from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from base.models import Match
from base.serializers.match_serializers import *

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_matches(request):
    matchs = Match.objects.all()
    serializer = MatchSerializer(matchs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_match(request, pk):
    try:
        match = Match.objects.get(pk = pk)
        serializer = MatchSerializer(match, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No match found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_match(request, pk):    
    try:
        Match(pk = pk).delete()
        message = {'detail': 'The match deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No match found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_match(request, pk):
    data = request.data
    # "1956-10-19 13:54:00"
    date = None
    if data.get('date_time') != None:
        y = int(data['date_time'][:4])
        m = int(data['date_time'][5:7])
        d = int(data['date_time'][8:10])
        h = int(data['date_time'][11:13])
        mm = int(data['date_time'][14:16])
        s = int(data['date_time'][17:])
        date = datetime(y, m, d, h, mm, s)
    try:
        match = Match.objects.get(pk = pk)
        if data.get('date_time') != None: match.date_time = date
        if data.get('host_players') != None: match.host_players = data['host_players']
        if data.get('away_players') != None: match.away_players = data['away_players']
        if data.get('weather') != None: match.weather = data['weather']
        if data.get('referee_kit_number') != None: match.referee_kit_number = data['referee_kit_number']
        if data.get('ticket_price') != None: match.ticket_price = data['ticket_price']
        match.save()
        serializer = MatchSerializer(match, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating match'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_match(request):
    data = request.data
    # "1956-10-19 13:54:00"
    date = None
    if data.get('date_time') != None:
        y = int(data['date_time'][:4])
        m = int(data['date_time'][5:7])
        d = int(data['date_time'][8:10])
        h = int(data['date_time'][11:13])
        mm = int(data['date_time'][14:16])
        s = int(data['date_time'][17:])
        date = datetime(y, m, d, h, mm, s)
    try :
        match = Match.objects.create(
            date_time = date,
            host_players = data['host_players'],
            away_players = data['away_players'],
            weather = data['weather'],
            referee_kit_number = data['referee_kit_number'],
            ticket_price = data['ticket_price'],
            
            host_club_id = int(data['host_club']),
            guest_club_id = int(data['guest_club']),
            stadium_id = int(data['stadium']),
            referee_id = int(data['referee']),
            first_referee_asist_id = int(data['first_referee_asist']),
            second_referee_asist_id = int(data['second_referee_asist_asist']),
            fourth_official_id = int(data['fourth_official']),
        )
        serializer = MatchSerializer(match, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while add match'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)