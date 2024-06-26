from rest_framework import serializers
from base.models import Employee
from base.serializers.user_serializers import SimpleUserSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField(read_only=True)

    def get_employee(self, obj):
        user = obj.employee
        serializer = SimpleUserSerializer(user, many=False)
        
        return serializer.data

    class Meta:
        model = Employee
        fields = '__all__'