from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

from base.models import SamplePlayer
from base.serializers.overview_serializers import PlayersOverviewSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_players(request):
    season = int(request.GET.get('se'))
    club = int(request.GET.get('cl'))
    
    players = SamplePlayer.objects.filter(club__season__season_id=season)
    if club != -1 : 
        players = players.filter(club__club__club_id=club)
    
    serializer = PlayersOverviewSerializer(players, many=True).data
    return Response(serializer)