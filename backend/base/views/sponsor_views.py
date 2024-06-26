from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Sponsor
from base.serializers.sponsor_serializers import SponsorSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_sponsors(request):
    sponsors = Sponsor.objects.all()
    serializer = SponsorSerializer(sponsors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_sponsor(request, pk):
    try:
        sponsor = Sponsor.objects.get(pk = pk)
        serializer = SponsorSerializer(sponsor, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_sponsor(request, pk):    
    try:
        Sponsor(pk = pk).delete()
        message = {'detail': 'The sponsor deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_sponsor(request, pk):
    data = request.data
    try:
        sponsor = Sponsor.objects.get(pk = pk)
        if data.get('name') != None: sponsor.name = data['name']
        if data.get('logo') != None: sponsor.logo = data['logo']
        if data.get('website') != None: sponsor.website = data['website']
        sponsor.save()
        serializer = SponsorSerializer(sponsor, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating sponsor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_sponsor(request):
    data = request.data
    try:
        sponsor = Sponsor.objects.create(
            name = data['name'],
            logo = data['logo'],
            website = data['website'],
        )
        serializer = SponsorSerializer(sponsor, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating sponsor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)