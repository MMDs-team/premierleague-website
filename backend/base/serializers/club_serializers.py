from rest_framework import serializers
from base.models import Club, ClubStaff, SampleClub, Stadium
from base.serializers.user_serializers import SimpleUserSerializer
from base.serializers.season_serializers import SeasonSerializer
from base.serializers.stadium_serializers import StadiumSerializer


class ClubSerializer(serializers.ModelSerializer):
    main_stadium = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Club
        fields = [
            'club_id', 'name', 'image', 'description',
            'est_date', 'website', 'social_media', 'email', 'main_stadium'
        ]
    
    def get_main_stadium(request, obj):
        main_stadium = obj.main_stadium
        serializer = StadiumSerializer(main_stadium, many=False)


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
        season = obj.season
        serializer = SeasonSerializer(season, many=False)
        return serializer.data
    


class SampleClubSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = SampleClub
        fields = '__all__'
    

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
    



class ClubOfLastSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club_id', 'name', 'website']

class SampleClubOfLastSeasonSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SampleClub
        fields = ['logo', 'club', 'sample_club_id']
    
    def get_club(self, obj):
        club = obj.club
        serializer = ClubOfLastSeasonSerializer(club, many=False)
        return serializer.data