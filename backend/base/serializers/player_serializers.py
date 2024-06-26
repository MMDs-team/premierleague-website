from rest_framework import serializers
from base.models import Player

from base.serializers.user_serializers import SimpleUserSerializer

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