from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Sponsor, ClubSpon, MatchSpon, SeaSpon
from base.serializers.sponsor_serializers import SponsorSerializer, ClubSponSerializer, MatchSponSerializer, SeaSponSerializer


############################ sponsor ############################

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
   
   
############################ clubSpon ############################
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_club_spons(request):
    club_spons = ClubSpon.objects.all()
    serializer = ClubSponSerializer(club_spons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_club_spon(request, pk):
    try:
        club_spon = ClubSpon.objects.get(pk = pk)
        serializer = ClubSponSerializer(club_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No club sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_club_spon(request, pk):    
    try:
        ClubSpon(pk = pk).delete()
        message = {'detail': 'The club sponsor deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No club sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_club_spon(request):
    data = request.data
    try:
        club_spon = ClubSpon.objects.create(
            club_id = data['club'],
            sponsor_id = data['sponsor'],
        )
        serializer = ClubSponSerializer(club_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating club sponsor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
############################ matchSpon ############################
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_match_spons(request):
    match_spons = MatchSpon.objects.all()
    serializer = MatchSponSerializer(match_spons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_match_spon(request, pk):
    try:
        match_spon = MatchSpon.objects.get(pk = pk)
        serializer = MatchSponSerializer(match_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No match sponor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_match_spon(request, pk):    
    try:
        MatchSpon(pk = pk).delete()
        message = {'detail': 'The match sponor deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No match sponor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_match_spon(request, pk):
    data = request.data
    try:
        match_spon = MatchSpon.objects.get(pk = pk)
        if data.get('amount') != None: match_spon.amount = data['amount']
        if data.get('gif') != None: match_spon.gif = data['gif']
        match_spon.save()
        serializer = MatchSponSerializer(match_spon, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating match sponor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_match_spon(request):
    data = request.data
    try:
        match_spon = MatchSpon.objects.create(
            amount = data['amount'],
            gif = data['gif'],
            
            match_id = data['match'],
            sponsor_id = data['sponsor'],
        )
        serializer = MatchSponSerializer(match_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating match sponor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
  
    
############################ seaSpon ############################
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_sea_spons(request):
    sea_spons = SeaSpon.objects.all()
    serializer = SeaSponSerializer(sea_spons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_single_sea_spon(request, pk):
    try:
        sea_spon = SeaSpon.objects.get(pk = pk)
        serializer = SeaSponSerializer(sea_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No season sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def remove_sea_spon(request, pk):    
    try:
        SeaSpon(pk = pk).delete()
        message = {'detail': 'The season sponsor deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    except :
        message = {'detail': 'No season sponsor found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def update_sea_spon(request, pk):
    data = request.data
    try:
        sea_spon = SeaSpon.objects.get(pk = pk)
        if data.get('image') != None: sea_spon.image = data['image']
        if data.get('amount') != None: sea_spon.amount = data['amount']
        if data.get('link') != None: sea_spon.link = data['link']
        sea_spon.save()
        serializer = SeaSponSerializer(sea_spon, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating season sponsor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
# @permission_classes([IsAdminUser])
def add_sea_spon(request):
    data = request.data
    try:
        sea_spon = SeaSpon.objects.create(
            image = data['image'],
            amount = data['amount'],
            link = data['link'],
            
            sponsor_id = data['sponsor'],
            season_id = data['season'],
        )
        serializer = SeaSponSerializer(sea_spon, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'Error while creating season sponsor'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)