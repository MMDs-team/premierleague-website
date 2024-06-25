from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import datetime

from base.models import Club, ClubStaff
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


@api_view(['PUT'])
def update_club(request, pk):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('est_date') != None:
        y = int(data['est_date'][:4])
        m = int(data['est_date'][5:7])
        d = int(data['est_date'][8:])
        date = datetime.date(y, m, d)

    try:
        club = Club.objects.get(pk = pk)

        if data.get('description') != None: club.description = data['description']
        if data.get('social_media') != None: club.social_media = data['social_media']
        if data.get('website')  != None: club.website = data['website']
        if data.get('image') != None: club.image = data['image']
        if data.get('email') != None: club.email = data['email']
        if data.get('name') != None: club.name = data['name']
        if date != None: club.est_date = date

        club.save()

        serializer = ClubSerializer(club, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating club'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_club(request, pk):
    message, stat = None, None
    try:
        Club(pk = pk).delete()
        message = {'detail': 'The club deleted successfully.'}
        stat = status.HTTP_200_OK
    except:
        message = {'detail': 'Error while deleting club'}
        stat = status.HTTP_400_BAD_REQUEST
    return Response(message, status=stat)

    
@api_view(['GET'])
def get_all_staff(request):
    all_club_staff = ClubStaff.objects.all()
    serializer = ClubStaffSerializer(all_club_staff, many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def add_staff(request):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('est_date') != None:
        y = int(data['est_date'][:4])
        m = int(data['est_date'][5:7])
        d = int(data['est_date'][8:])
        date = datetime.date(y, m, d)

    club_staff = ClubStaff.objects.create(
        club_id = int(data['club']),
        staff_id = int(data['user']),
        position = data['position'],
        description = data['description'],
        image = data['image'],
        birth_date = date
    )

    serializer = ClubStaffSerializer(club_staff, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_staff(request, pk):
    try:
        club_staff = ClubStaff.objects.get(pk = pk)
        serializer = ClubStaffSerializer(club_staff, many=False)
        return Response(serializer.data)
    except :
        message = {'detail': 'No Staff found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['DELETE'])
def remove_staff(request, pk):
    message, stat = None, None
    try:
        ClubStaff(pk = pk).delete()
        message = {'detail': 'The club staff deleted successfully.'}
        stat = status.HTTP_200_OK
    except:
        message = {'detail': 'Error while deleting club staff'}
        stat = status.HTTP_400_BAD_REQUEST
    return Response(message, status=stat)


@api_view(['PUT'])
def update_staff(request, pk):
    data = request.data
    # "1956-10-19"
    date = None
    if data.get('est_date') != None:
        y = int(data['est_date'][:4])
        m = int(data['est_date'][5:7])
        d = int(data['est_date'][8:])
        date = datetime.date(y, m, d)

    try:
        club_staff = ClubStaff.objects.get(pk = pk)

        if data.get('description') != None: club_staff.description = data['description']
        if data.get('position') != None: club_staff.position = data['position']
        if data.get('website')  != None: club_staff.website = data['website']
        if data.get('image') != None: club_staff.image = data['image']
        if data.get('club') != None: club_staff.club_id = data['club']
        if data.get('user') != None: club_staff.staff_id = data['user']
        if date != None: club_staff.est_date = date

        club_staff.save()

        serializer = ClubStaffSerializer(club_staff, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error while updating club staff'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
