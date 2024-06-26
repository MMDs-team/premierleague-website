from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base.models import Kit
from base.serializers.kit_serializers import *


@api_view(['GET'])
def get_all_kits(request):
    kits = Kit.objects.all()
    serializers = KitSerializer(kits, many=True)

    return Response(serializers.data)


@api_view(['GET'])
def get_single_kit(request, pk):
    kit = Kit.objects.filter(pk=pk).first()
    
    if kit is None: return Response({
        'detail': "Kit with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)
    
    serializer = KitSerializer(kit, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_kit(request, pk):
    kit = Kit.objects.filter(pk=pk).first()
    if kit is None: return Response({
        'detail': "Kit with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)
    kit.delete()

    return Response({
        'detail': f"Kit with id={pk} have been deleted!"
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_kit(request, pk):
    kit = Kit.objects.filter(pk=pk).first()
    if kit is None: return Response({
        'detail': "Kit with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)


    '''
        fields we can change: image, color, sample_club
    '''
    data = request.data
    if data.get('kit_id') is not None: return Response({
        'detail': "You can not change the primary key!"
    }, status=status.HTTP_400_BAD_REQUEST)

    if data.get('image') is not None: kit.image = data['image']
    if data.get('color') is not None: kit.color = data['color'].lower()
    if data.get('sample_club') is not None: kit.sample_club = int(data['sample_club'])

    serializer = KitSerializer(kit, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_kit(request):
    data = request.data
    print(type(data.get('image')))
    if data.get('image') is None or \
        data.get('color') is None or \
        data.get('sample_club') is None: return Response({
            'detail': 'Some mandatory fields of request is missing!'
        }, status=status.HTTP_400_BAD_REQUEST)

    kit = Kit() if data.get('kit_id') is None else Kit(pk=int(data['kit_id']))
    kit.image = data['image']
    kit.color = data['color'].lower()
    kit.sample_club_id = int(data['sample_club'])
    kit.save()

    serializer = KitSerializer(kit, many=False)
    return Response(serializer.data)