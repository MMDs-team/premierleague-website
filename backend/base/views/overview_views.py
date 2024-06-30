from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from bisect import bisect_left, bisect_right
from django.db.models import Q
import datetime

from base.models import Match, SamplePlayer, SampleClub, Club, Action
from base.serializers.overview_serializers import *


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


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def season_clubs(request):
    season = int(request.GET.get('se'))
    clubs = SampleClub.objects.filter(club__season__season_id=season)
    serializer = SeasonClubsOverviewSerializer(clubs, many=True).data
    return Response(serializer)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def all_clubs(request):
    clubs = Club.objects.all()
    serializer = AllClubsOverviewSerializer(clubs, many=True).data
    return Response(serializer)


@api_view(['GET'])
def get_fixtures(request):
    sample_club = int(request.GET['s_cl'])

    matches = Match.objects.all()
    if sample_club != -1: 
        matches = matches.filter(Q(host_club=sample_club) | Q(guest_club=sample_club))

    matches = list(matches.order_by('date_time'))
    if not matches: return Response({})

    result = []
    curr_date = matches[0].date_time.date()
    while True:
        left = bisect_left(matches, curr_date, key=lambda x: x.date_time.date())
        right = bisect_right(matches, curr_date, key=lambda x: x.date_time.date())

        result.append({'date': curr_date, 'matches': []})
        today_matches = result[-1]
        today_matches['matches'] = [MatchSerializerForFixtures(match).data for match in matches[left:right]]

        if right < len(matches): curr_date = matches[right].date_time.date()
        else: break
    
    return Response(result)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_tables(request):
    serializer = table_serializer(request)
    return Response(serializer)