from rest_framework import serializers
from base.models import Kit
from base.serializers.club_serializers import SampleClubSerializer

class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = '__all__'