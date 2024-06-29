from rest_framework import serializers
from base.models import SampleClub, Player, SamplePlayer

class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = ['name', 'logo']


class SamplePlayerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    position = serializers.CharField(source='player.position', read_only=True)
    sample_club = serializers.SerializerMethodField(read_only=True)
    nationality = serializers.CharField(source='player.nationality')

    def get_sample_club(self, obj):
        sample_club = obj.club
        serializer = SampleClubSerializer(sample_club, many=False)

        return serializer.data

    class Meta:
        model = SamplePlayer
        fields = [
            'first_name',
            'last_name',
            'sample_club',
            'position',
            'nationality'
        ]

class PlayerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.last_name', read_only=True)

    class Meta:
        model = Player
        fields = [
            'first_name',
            'last_name',
            'position',
            'nationality'
        ]
    