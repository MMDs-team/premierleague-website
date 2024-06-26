from rest_framework import serializers
from base.models import Kit
from base.serializers.club_serializers import SampleClubSerializer

class KitSerializer(serializers.ModelSerializer):
    sample_club = serializers.SerializerMethodField(read_only=True)

    def get_sample_club(self, obj):
        sample_club = obj.sample_club
        serializer = SampleClubSerializer(sample_club, many=False)

        return serializer.data

    class Meta:
        model = Kit
        fields = '__all__'