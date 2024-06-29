from rest_framework import serializers
from base.models import SampleClub

class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = ['name', 'logo']