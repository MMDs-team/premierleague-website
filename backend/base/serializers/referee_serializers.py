from rest_framework import serializers
from base.models import Referee

from base.serializers.user_serializers import SimpleUserSerializer

class RefereeSerializer(serializers.ModelSerializer):
    referee = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Referee
        fields = [
            'referee', 'image', 'birth_date',
            'nationality', 'cv',
        ]
        
    def get_referee(self, obj):
        user = obj.referee
        serializer = SimpleUserSerializer(user, many=False)
        return serializer.data