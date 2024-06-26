from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

from base.models import Referee
from base.serializers.referee_serializers import *

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_referees(request):
    referee = Referee.objects.all()
    serializer = RefereeSerializer(referee, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_referee(request, pk):
    try:
        referee = Referee.objects.get(pk = pk)
        serializer = RefereeSerializer(referee, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No referee found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_referee(request, pk):    
    try:
        Referee(pk = pk).delete()
        message = {'detail': 'The referee deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No referee found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_referee(request, pk):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('birth_date') != None:
        y = int(data['birth_date'][:4])
        m = int(data['birth_date'][5:7])
        d = int(data['birth_date'][8:])
        date = datetime.date(y, m, d)
    try:
        referee = Referee.objects.get(pk = pk)
        if data.get('image') != None: referee.image = data['image']
        if data.get('birth_date') != None: referee.birth_date = date
        if data.get('nationality') != None: referee.nationality = data['nationality']
        if data.get('cv') != None: referee.cv = data['cv']
        referee.save()
        serializer = RefereeSerializer(referee, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating referee'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_referee(request):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('birth_date') != None:
        y = int(data['birth_date'][:4])
        m = int(data['birth_date'][5:7])
        d = int(data['birth_date'][8:])
        date = datetime.date(y, m, d)
    try :
        referee = Referee.objects.create(
            referee_id = int(data['user']),
            image = data['image'],
            birth_date = date,
            nationality = data['nationality'],
            cv = data['cv'],
        )
        serializer = RefereeSerializer(referee, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while add referee'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)