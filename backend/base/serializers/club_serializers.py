from rest_framework import serializers
from base.models import Club, ClubStaff, SampleClub
from base.serializers.user_serializers import SimpleUserSerializer
from base.serializers.season_serializers import SeasonSerializer



class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = [
            'club_id', 'name', 'image', 'description',
            'est_date', 'website', 'social_media', 'email'
        ]


class SampleClubSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField(read_only=True)
    season = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SampleClub
        fields = '__all__'
    
    def get_club(self, obj):
        club = obj.club
        serializer = ClubSerializer(club, many=False)
        return serializer.data
    
    def get_season(self, obj):
        season = obj.staff
        serializer = SeasonSerializer(season, many=False)
        return serializer.data
    



class ClubStaffSerializer(serializers.ModelSerializer):

    staff = serializers.SerializerMethodField(read_only=True)
    club = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ClubStaff
        fields = '__all__'

    def get_staff(self, obj):
        user = obj.staff
        serializer = SimpleUserSerializer(user, many=False)
        return serializer.data
    
    def get_club(self, obj):
        club = obj.club
        serializer = SampleClubSerializer(club, many=False)
        return serializer.data
    
