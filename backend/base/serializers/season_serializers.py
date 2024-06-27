from rest_framework import serializers
from base.models import Season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
        fields = [
            'season_id',
            'cup_image',
            'date',
            'kit1',
            'kit2',
            'kit3',
            'kit4'
        ]