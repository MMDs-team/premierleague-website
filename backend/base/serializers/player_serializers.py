from rest_framework import serializers
from base.models import Player, SamplePlayer

from base.serializers.user_serializers import SimpleUserSerializer
from base.serializers.club_serializers import SampleClubSerializer

class PlayerSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Player
        fields = [
            'player', 'image', 'birth_date', 'nationality', 
            'height', 'social_media', 'position', 'heath_state'
        ]
        
    def get_player(self, obj):
        user = obj.player
        serializer = SimpleUserSerializer(user, many=False)
        return serializer.data
    
    
class SamplePlayerSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField(read_only=True)
    club = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = SamplePlayer
        fields = [
            'sample_player_id', 'player', 'club', 
            'number_in_team', 'position',
        ]
        
    def get_player(self, obj):
        user = obj.player
        serializer = PlayerSerializer(user, many=False)
        return serializer.data
    
    def get_club(self, obj):
        user = obj.club
        serializer = SampleClubSerializer(user, many=False)
        return serializer.data