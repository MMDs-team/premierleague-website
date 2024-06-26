from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Stadium
from base.serializers.stadium_serializers import *



@api_view(['GET'])
def get_all_stadiums(request):
    stadiums = Stadium.objects.all()
    serializer = StadiumSerializer(stadiums, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def get_single_stadium(request, pk):
    try:
        stadium = Stadium.objects.get(pk = pk)
        serializer = StadiumSerializer(stadium, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No stadium found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def add_stadium(request):
    data = request.data

    try:
        stadium = Stadium.objects.create(
            name = data['name'],
            city = data['city'],
            image = data['image'],
            address = data['address'],
            coordinates = data['coordinates'],
            capacity = data['capacity'],
            description = data['description']
        )

        serializer = StadiumSerializer(stadium, many=False)

        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating stadium'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def update_stadium(request, pk):
    data = request.data

    try:
        stadium = Stadium.objects.get(pk = pk)

        if data.get('name') != None: stadium.name = data['name']
        if data.get('city') != None: stadium.city = data['city']
        if data.get('website')  != None: stadium.website = data['website']
        if data.get('image') != None: stadium.image = data['image']
        if data.get('address') != None: stadium.address = data['address']
        if data.get('coordinates') != None: stadium.coordinates = data['coordinates']
        if data.get('capacity') != None: stadium.capacity = data['capacity']
        if data.get('description') != None: stadium.description = data['description']

        stadium.save()

        serializer = StadiumSerializer(stadium, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating stadium'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def remove_stadium(request, pk):
    message, stat = None, None
    try:
        Stadium(pk = pk).delete()
        message = {'detail': 'The stadium deleted successfully.'}
        stat = status.HTTP_200_OK
    except:
        message = {'detail': 'Error while deleting stadium'}
        stat = status.HTTP_400_BAD_REQUEST
    return Response(message, status=stat)