from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

from base.models import Player, SamplePlayer
from base.serializers.player_serializers import *

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_player(request, pk):
    try:
        player = Player.objects.get(pk = pk)
        serializer = PlayerSerializer(player, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No player found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_player(request, pk):    
    try:
        Player(pk = pk).delete()
        message = {'detail': 'The player deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No player found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_player(request, pk):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('birth_date') != None:
        y = int(data['birth_date'][:4])
        m = int(data['birth_date'][5:7])
        d = int(data['birth_date'][8:])
        date = datetime.date(y, m, d)
    try:
        player = Player.objects.get(pk = pk)
        if data.get('image') != None: player.image = data['image']
        if data.get('birth_date') != None: player.birth_date = date
        if data.get('nationality') != None: player.nationality = data['nationality']
        if data.get('height') != None: player.height = data['height']
        if data.get('social_media') != None: player.social_media = data['social_media']
        if data.get('position') != None: player.position = data['position']
        if data.get('heath_state') != None: player.heath_state = bool(int(data['heath_state']))
        player.save()
        serializer = PlayerSerializer(player, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating player'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_player(request):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('birth_date') != None:
        y = int(data['birth_date'][:4])
        m = int(data['birth_date'][5:7])
        d = int(data['birth_date'][8:])
        date = datetime.date(y, m, d)
    try :
        player = Player.objects.create(
            player_id = int(data['user']),
            image = data['image'],
            birth_date = date,
            nationality = data['nationality'],
            height = data['height'],
            social_media = data['social_media'],
            position = data['position'],
            heath_state = bool(int(data['heath_state'])),
        )
        serializer = PlayerSerializer(player, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while add player'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
     
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_sample_players(request):
    sample_players = SamplePlayer.objects.all()
    serializer = SamplePlayerSerializer(sample_players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_sample_player(request, pk):
    try:
        sample_player = SamplePlayer.objects.get(pk = pk)
        serializer = SamplePlayerSerializer(sample_player, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No sample_player found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_sample_player(request, pk):    
    try:
        SamplePlayer(pk = pk).delete()
        message = {'detail': 'The sample player deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No sample player found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_sample_player(request, pk):
    data = request.data
    try:
        sample_player = SamplePlayer.objects.get(pk = pk)
        if data.get('number_in_team') != None: sample_player.number_in_team = data['number_in_team']
        if data.get('position') != None: sample_player.position = data['position']
        sample_player.save()
        serializer = SamplePlayerSerializer(sample_player, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating sample player'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_sample_player(request):
    data = request.data
    try :
        sample_player = SamplePlayer.objects.create(
            club_id = int(data['club']),
            player_id = int(data['player']),
            number_in_team = int(data['number_in_team']),
            position = data['position'],
        )
        serializer = SamplePlayerSerializer(sample_player, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while add sample player'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)