from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

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
        club = Club.objects.get(pk = pk)
        serializer = ClubSerializer(club, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No Club found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['POST'])
def add_club(request):
    data = request.data
    # "1956-10-19"
    y = int(data['est_date'][:4])
    m = int(data['est_date'][5:7])
    d = int(data['est_date'][8:])
    print("year=", y)
    print("mounth=", m)
    print("day=", d)
    date = datetime.date(y, m, d)

    try:
        club = Club.objects.create(
            name = data['name'],
            image = data['image'],
            description = data['description'],
            est_date = date,
            website = data['website'],
            social_media = data['social_media'],
            email = data['email']
        )

        serializer = ClubSerializer(club, many=False)

        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating club'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


