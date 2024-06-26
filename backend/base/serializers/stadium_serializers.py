from rest_framework import serializers
from base.models import Stadium, ClubStad
from base.serializers.club_serializers import ClubSerializer



class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'


class ClubStadiumSerializer(serializers.ModelSerializer):
    club = serializers.SerializerMethodField(read_only=True)
    stadium = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Stadium
        fields = ['club', 'stadium']

    def get_club(self, obj):
        club = obj.club
        serializer = ClubSerializer(club, many=False)
        return serializer.data
    
    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)
        return serializer.data