from base.models import Match
from rest_framework import serializers

class MatchSerializerForFixtures(serializers.ModelSerializer):
    time = serializers.SerializerMethodField(read_only=True)
    
    def get_time(self, obj):
        return obj.date_time.time()
        
    class Meta:
        model = Match
        fields = [
            'match_id',
            'time',
            'ticket_price',
            'result',
            'host_club',
            'guest_club',
            'stadium'
        ]