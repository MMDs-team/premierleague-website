from rest_framework import serializers
from base.models import Match

from base.serializers.club_serializers import SampleClubSerializer
from base.serializers.stadium_serializers import StadiumSerializer
from base.serializers.referee_serializers import RefereeSerializer

class MatchSerializer(serializers.ModelSerializer):
    host_club = serializers.SerializerMethodField(read_only=True)
    guest_club = serializers.SerializerMethodField(read_only=True)
    stadium = serializers.SerializerMethodField(read_only=True)
    referee = serializers.SerializerMethodField(read_only=True)
    first_referee_asist = serializers.SerializerMethodField(read_only=True)
    second_referee_asist = serializers.SerializerMethodField(read_only=True)
    fourth_official = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Match
        fields = [
            'match_id', 'date_time', 'host_players', 'away_players', 
            'weather', 'referee_kit_number', 'ticket_price','result',
            
            'host_club', 'guest_club', 'stadium', 'referee',
            'first_referee_asist', 'second_referee_asist',
            'fourth_official'
        ]
        
    def get_host_club(self, obj):
        club = obj.host_club
        serializer = SampleClubSerializer(club, many=False)
        return serializer.data
    
    def get_guest_club(self, obj):
        club = obj.guest_club
        serializer = SampleClubSerializer(club, many=False)
        return serializer.data

    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)
        return serializer.data
    
    def get_referee(self, obj):
        referee = obj.referee
        serializer = RefereeSerializer(referee, many=False)
        return serializer.data
    
    def get_first_referee_asist(self, obj):
        referee = obj.first_referee_asist
        serializer = RefereeSerializer(referee, many=False)
        return serializer.data
    
    def get_second_referee_asist(self, obj):
        referee = obj.second_referee_asist
        serializer = RefereeSerializer(referee, many=False)
        return serializer.data
    
    def get_fourth_official(self, obj):
        referee = obj.fourth_official
        serializer = RefereeSerializer(referee, many=False)
        return serializer.data