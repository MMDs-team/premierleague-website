from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base.models import Season
from base.serializers.season_serializers import *
import datetime


@api_view(['GET'])
def get_all_seasons(request):
    seasons = Season.objects.all()
    serializers = SeasonSerializer(seasons, many=True)

    return Response(serializers.data)


@api_view(['GET'])
def get_single_season(request, pk):
    season = Season.objects.filter(pk=pk).first()

    if season is None: return Response({
        'detail': "Season with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    serializer = SeasonSerializer(season, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_season(request, pk):
    season = Season.objects.filter(pk=pk).first()
    if season is None: return Response({
        'detail': "Season with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)

    season.delete()
    return Response({
        'detail': f"Season with id={pk} have been deleted!"
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_season(request, pk):
    season = Season.objects.filter(pk=pk).first()
    if season is None: return Response({
        'detail': "Season with given id doesn't exists!"
    }, status=status.HTTP_204_NO_CONTENT)


    '''
        fields we can change: cup_image, date, 
            kit1, kit2, kit3, kit4
    '''
    data = request.data
    if data.get('season_id') is not None: return Response({
        'detail': "You can not change the primary key!"
    }, status=status.HTTP_400_BAD_REQUEST)

    if data.get('cup_image') is not None: season.cup_image = data['cup_image']
    if data.get('date') is not None: season.date = data['date']
    if data.get('kit1') is not None: season.kit1_id = int(data['kit1'])
    if data.get('kit2') is not None: season.kit2_id = int(data['kit2'])
    if data.get('kit3') is not None: season.kit3_id = int(data['kit3'])
    if data.get('kit4') is not None: season.kit4_id = int(data['kit4'])
    season.save()

    serializer = SeasonSerializer(season, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_season(request):
    data = request.data
    if data.get('date') is None: return Response({
            'detail': 'Date field is missing!'
        }, status=status.HTTP_400_BAD_REQUEST)

    season = Season() if data.get('season_id') is None else Season(pk=int(data['season_id']))
    year, month, day = int(data['date'][:4]), int(data['date'][5:7]), int(data['date'][8:])
    season.date = datetime.date(year, month, day)

    if data.get('cup_image') is not None: season.cup_image = data['cup_image']
    if data.get('date') is not None: season.date = data['date']
    if data.get('kit1') is not None: season.kit1_id = int(data['kit1'])
    if data.get('kit2') is not None: season.kit2_id = int(data['kit2'])
    if data.get('kit3') is not None: season.kit3_id = int(data['kit3'])
    if data.get('kit4') is not None: season.kit4_id = int(data['kit4'])
    season.save()

    serializer = SeasonSerializer(season, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_seasons_by_order(request):
    result = Season.objects.order_by('date').values('season_id', 'date')
    return Response(result)