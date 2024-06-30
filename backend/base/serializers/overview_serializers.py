from rest_framework import serializers
from base.models import SamplePlayer, Match, SampleClub, Club, Stadium

class PlayersOverviewSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    nationality = serializers.CharField(source='player.nationality', read_only=True)
    image = serializers.FileField(source='player.image', read_only=True)

    class Meta:
        model = SamplePlayer
        fields = (
            'sample_player_id',
            'first_name',
            'last_name', 
            'position',
            'nationality',
            'image',
        )
        
        
class SeasonClubsOverviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = (
            'sample_club_id',
            'name',
            'logo',
        )
   
class AllClubsOverviewSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField(read_only=True)
    main_stadium = serializers.SerializerMethodField(read_only=True)
    
    def get_logo(self, obj):
        logo = SampleClub.objects.filter(club=obj.club_id).latest('season').logo
        return logo.url
    
    def get_main_stadium(self, obj):
        return obj.main_stadium.name
    
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'logo',
            'main_stadium_id',
            'main_stadium',
        )
    

class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name')
    class Meta:
        model = SampleClub
        fields = [
            'name',
            'logo'
        ]

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = [
            'name',
            'city'
        ]
        
class MatchSerializerForFixtures(serializers.ModelSerializer):
    time = serializers.SerializerMethodField(read_only=True)
    host_club = serializers.SerializerMethodField(read_only=True)
    guest_club = serializers.SerializerMethodField(read_only=True)
    stadium = serializers.SerializerMethodField(read_only=True)
    
    def get_time(self, obj):
        return obj.date_time.time()
    
    def get_host_club(self, obj):
        host_club = obj.host_club
        serializer = SampleClubSerializer(host_club, many=False)

        return serializer.data

    def get_guest_club(self, obj):
        guest_club = obj.guest_club
        serializer = SampleClubSerializer(guest_club, many=False)

        return serializer.data
    
    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)
        
        return serializer.data
        
    class Meta:
        model = Match
        fields = [
            'match_id',
            'time',
            'ticket_price',
            'result',
            'host_club',
            'guest_club',
            'stadium'
        ]