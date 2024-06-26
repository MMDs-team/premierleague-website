from rest_framework import serializers
from base.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField(read_only=True)

    def get_employee(self, obj): return obj.employee

    class Meta:
        model = Employee
        fields = '__all__'