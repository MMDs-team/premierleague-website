from rest_framework import serializers
from base.models import TicketType, Ticket
from base.serializers.stadium_serializers import StadiumSerializer
from base.serializers.user_serializers import SimpleUserSerializer
from base.serializers.match_serializers import MatchSerializer



class TicketSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    match = serializers.SerializerMethodField(read_only=True)
    stadium = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Ticket
        fields = '__all__'
    
    def get_user(self, obj):
        user = obj.user
        serializer = SimpleUserSerializer(user, many=False)

        return serializer.data

    def get_match(self, obj):
        match = obj.match
        serializer = MatchSerializer(match, many=False)

        return serializer.data
    
    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)

        return serializer.data   
     


class TicketTypeSerializer(serializers.ModelSerializer):
    stadium = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TicketType
        fields = [  'type_id', 'ratio', 's_number',
                    'e_number', 'color', 'description',
                    'stadium', 'html_tag_id'
                ]

    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)

        return serializer.data
    

