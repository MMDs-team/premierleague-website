from rest_framework import serializers
from base.models import Kit

class KitSerializer(serializers.ModelSerializer):
    sample_club = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Kit
        fields = '__all__'