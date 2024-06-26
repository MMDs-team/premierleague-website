from rest_framework import serializers
from base.models import Sponsor, ClubSpon, MatchSpon, SeaSpon

from base.serializers.club_serializers import ClubSerializer
from base.serializers.match_serializers import MatchSerializer
from base.serializers.season_serializers import SeasonSerializer

class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = '__all__'
        
        
class ClubSponSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField(read_only=True)
    sponsor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ClubSpon
        fields = '__all__'
        
    def get_club(self, obj):
        club = obj.club
        serializer = ClubSerializer(club, many=False)
        return serializer.data
    
    def get_sponsor(self, obj):
        sponsor = obj.sponsor
        serializer = SponsorSerializer(sponsor, many=False)
        return serializer.data
        

class MatchSponSerializer(serializers.ModelSerializer):
    match = serializers.SerializerMethodField(read_only=True)
    sponsor = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = MatchSpon
        fields = '__all__'
        
    def get_match(self, obj):
        match = obj.match
        serializer = MatchSerializer(match, many=False)
        return serializer.data
    
    def get_sponsor(self, obj):
        sponsor = obj.sponsor
        serializer = SponsorSerializer(sponsor, many=False)
        return serializer.data
        
        
class SeaSponSerializer(serializers.ModelSerializer):
    season = serializers.SerializerMethodField(read_only=True)
    sponsor = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = SeaSpon
        fields = '__all__'
        
    def get_season(self, obj):
        season = obj.season
        serializer = SeasonSerializer(season, many=False)
        return serializer.data
    
    def get_sponsor(self, obj):
        sponsor = obj.sponsor
        serializer = SponsorSerializer(sponsor, many=False)
        return serializer.data