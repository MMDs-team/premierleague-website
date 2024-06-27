from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base.models import Employee
from base.serializers.employee_serializers import *
import datetime


@api_view(['GET'])
def get_all_employees(request):
    employees = Employee.objects.all()
    serializers = EmployeeSerializer(employees, many=True)

    return Response(serializers.data)


@api_view(['GET'])
def get_single_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()

    if employee is None: return Response({
        'detail': "Employee with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    if employee is None: return Response({
        'detail': "Employee with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    employee.delete()
    return Response({
        'detail': f"Employee with id={pk} have been deleted!"
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_employee(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    if employee is None: return Response({
        'detail': "Employee with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)


    '''
        fields we can change: image, birth_date, position, description, 
            cv, salary, gender
    '''
    data = request.data
    if data.get('employee') is not None: return Response({
        'detail': "You can not change the primary key!"
    }, status=status.HTTP_400_BAD_REQUEST)

    if data.get('image') is not None: employee.image = data['image']
    if data.get('birth_date') is not None: 
        year, month, day = int(data['birth_date'][:4]), int(data['birth_date'][5:7]), int(data['birth_date'][8:])
        employee.birth_date = datetime.date(year, month, day)

    if data.get('position') is not None: employee.position = data['position']
    if data.get('description') is not None: employee.description = data['description']
    if data.get('cv') is not None: employee.cv = data['cv']
    if data.get('salary') is not None: employee.salary = float(data['salary'])
    if data.get('gender') is not None: employee.gender = bool(data['gender'])
    employee.save()

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_employee(request):
    data = request.data
    if data.get('employee') is None or \
        data.get('birth_date') is None or \
        data.get('position') is None or \
        data.get('description') is None or \
        data.get('cv') is None or \
        data.get('salary') is None or \
            data.get('gender') is None: return Response({
            'detail': 'Some required fields is missing!'
        }, status=status.HTTP_400_BAD_REQUEST)

    year, month, day = int(data['birth_date'][:4]), int(data['birth_date'][5:7]), int(data['birth_date'][8:])
    birth_date = datetime.date(year, month, day)

    employee = Employee(
        pk=int(data['employee']),
        birth_date=birth_date,
        position=data['position'],
        description=data['description'],
        cv=data['cv'],
        salary=float(data['salary']),
        gender=bool(data['gender'])
    )
    if data.get('image') is not None: employee.image = data['image']

    employee.save()

    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)