from rest_framework import serializers
from base.models import SamplePlayer

class PlayersOverviewSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    nationality = serializers.CharField(source='player.nationality', read_only=True)
    image = serializers.FileField(source='player.image', read_only=True)

    class Meta:
        model = SamplePlayer
        fields = (
            'sample_player_id', 'first_name', 'last_name', 
            'position', 'nationality', 'image',
        )