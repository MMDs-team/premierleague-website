from base.models import Action, ActionType
from base.serializers.match_serializers import MatchSerializer
from base.serializers.player_serializers import PlayerSerializer
from base.serializers.user_serializers import SimpleUserSerializer
from rest_framework import serializers

class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'
    
    
class ActionSerializer(serializers.ModelSerializer):
    action_type = serializers.SerializerMethodField(read_only=True)
    match = serializers.SerializerMethodField(read_only=True)
    subject = serializers.SerializerMethodField(read_only=True)
    object = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Action
        fields = '__all__'
    
    def get_action_type(self, obj):
        action_type = obj.action_type
        serializer = ActionTypeSerializer(action_type, many=False)

        return serializer.data

    def get_match(self, obj):
        match = obj.match
        serializer = MatchSerializer(match, many=False)

        return serializer.data
    
    def get_subject(self, obj):
        subject = obj.subject
        serializer = SimpleUserSerializer(subject, many=False)

        return serializer.data

    def get_object(self, obj):
        object = obj.object
        serializer = PlayerSerializer(object, many=False)

        return serializer.data