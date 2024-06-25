from rest_framework import serializers
from base.models import Club



class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = [
            'club_id', 'name', 'image', 'description',
            'est_date', 'website', 'social_media', 'email'
        ]