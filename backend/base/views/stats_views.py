from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Player
from base.serializers.stats_serializers import StatusTopPlayerAllTimeSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def status_top_player_all_time(request):
    players = Player.objects.all()
    serializer = StatusTopPlayerAllTimeSerializer(players)
    return Response(serializer)