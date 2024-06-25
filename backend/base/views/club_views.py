from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Club
from base.serializers.club_serializers import *

@api_view(['GET'])
def get_all_clubs(request):
    clubs = Club.objects.all()
    serializer = ClubSerializer(clubs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_single_club(request, pk):
    try:
        club = Club.objects.get(club_id = pk)
        serializer = ClubSerializer(club, many=False)
        return Response(serializer.data)
    except :
        return Response({'detail': 'No Club found with this id'}, status=status.HTTP_404_NOT_FOUND)
        
