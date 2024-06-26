from rest_framework import serializers
from base.models import Action

class ActionSerializer(serializers.ModelSerializer):
    action_type = serializers.SerializerMethodField(read_only=True)
    match = serializers.SerializerMethodField(read_only=True)
    subject = serializers.SerializerMethodField(read_only=True)
    object = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Action
        fields = '__all__'
    
    def get_action_type(self, obj): return obj.action_type

    def get_match(self, obj): return obj.match
    
    def get_subject(self, obj): return obj.subject

    def get_object(self, obj): return obj.object