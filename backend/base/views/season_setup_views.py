from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Season, Club, SampleClub, Match
import datetime
from django.db import transaction

from collections import deque

TEAMS_COUNT = 20

def check_if_unique(clubs):
    clubs = sorted(clubs)
    for i in range(1, len(clubs)):
        if clubs[i - 1] == clubs[i]: return False
    
    return True


@transaction.atomic()
def generate_matches(sample_clubs):
    today = datetime.now()
    for week in range(TEAMS_COUNT - 1):
        first_day = today + datetime.timedelta(weeks=week)
        for game in range(TEAMS_COUNT // 2):
            host = sample_clubs[game]
            guest = sample_clubs[TEAMS_COUNT - game - 1]

            # go:
            Match.objects.create(
                date_time=first_day,
                host_club_id=host.sample_club_id,
                guest_club_id=guest.sample_club_id,
                stadium=host.club.stadium
            )

            # return:
            Match.objects.create(
                date_time=first_day + datetime.timedelta(weeks=week + TEAMS_COUNT - 1),
                host_club_id=guest.sample_club_id,
                guest_club_id=host.sample_club_id,
                stadium=guest.club.stadium
            )

        sample_clubs = [sample_clubs[0]] + [sample_clubs[-1]] + sample_clubs[1:-1] 


@api_view(['GET'])
def setup_season(request):
    season_id = request.data['season_id']
    clubs = [int(club_id) for club_id in request.data['clubs'][1:-1].split(', ')]
    logos = list(request.FILES.values())

    if len(clubs) != len(logos) or len(clubs) != TEAMS_COUNT: return Response({
        'message': 'Input is not correct.'
    })
    if not check_if_unique(clubs): return Response({
        'message': f'clubs list must have {TEAMS_COUNT} unique club!'
    })

    season = Season.objects.filter(pk=season_id).first()
    if not season: return Response({
        'message': f'There is no Season record with id={season_id}'
    })

    sample_clubs = []
    for i in range(len(clubs)):
        club_id = clubs[i]
        club = Club.objects.filter(pk=club_id).first()
        if not club: return Response({
            'message': f'There is no Club record with id={club_id}'
        })

        sample_club = SampleClub.objects.create(
            season_id=season_id,
            club_id=club_id,
            logo=logos,
            # Give this field a default value
            total_points=0
        )
        sample_clubs.append(sample_club)

    generate_matches(sample_clubs)

    return Response({'message': 'Successful!'})