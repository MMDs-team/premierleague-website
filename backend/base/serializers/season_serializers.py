from rest_framework import serializers
from base.models import Season

class SeasonSerializer(serializers.ModelSerializer):
    kit1 = serializers.SerializerMethodField(read_only=True)
    kit2 = serializers.SerializerMethodField(read_only=True)
    kit3 = serializers.SerializerMethodField(read_only=True)
    kit4 = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Season
        fields = [
            'season_id',
            'cup_image',
            'date',
            'kit1',
            'kit2',
            'kit3',
            'kit4'
        ]
    
    def get_kit1(self, obj): return obj.kit1

    def get_kit2(self, obj): return obj.kit2
    
    def get_kit3(self, obj): return obj.kit3

    def get_kit4(self, obj): return obj.kit4