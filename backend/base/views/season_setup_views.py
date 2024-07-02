from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Season, Club, SampleClub, Match
import datetime as dt
from random import randint, shuffle
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
    matches = []
    today = dt.datetime.today()
    week_first_day = today + dt.timedelta(days=7) - dt.timedelta(dt.date.weekday(today))
    for week in range(TEAMS_COUNT - 1):
        first_day = week_first_day + dt.timedelta(weeks=week)
        for game in range(TEAMS_COUNT // 2):
            host = sample_clubs[game]
            guest = sample_clubs[TEAMS_COUNT - game - 1]

            host_stadium = host.club.main_stadium_id
            go_date_time = first_day + dt.timedelta(days=randint(0, 6)),
            matches.append([host.sample_club_id, guest.sample_club_id, go_date_time, host_stadium, True])

            guest_stadium = host.club.main_stadium_id
            ret_date_time = first_day + dt.timedelta(days=randint(0, 6)),
            matches.append([guest.sample_club_id, host.sample_club_id, ret_date_time, guest_stadium, True])


        sample_clubs = [sample_clubs[0]] + [sample_clubs[-1]] + sample_clubs[1:-1] 
    
    
    shuffle(matches)
    for sample_club in sample_clubs:
        sample_club_id = sample_club.sample_club_id

        prev1 = prev2 = None
        for i in range(len(matches)):
            curr_match = matches[i]
            if sample_club_id in (curr_match[0], curr_match[1]):
                if prev1 is None: prev1, prev2 = prev2, curr_match
                elif curr_match[4] == prev1[4] and prev1[4] == prev2[4]:
                    for j in range(i + 1, len(matches)):
                        if curr_match[4] != matches[j][4]: 
                            curr_match, matches[j], matches[j], curr_match
                            curr_match[2], matches[j][2] = matches[j][2], curr_match[2]
                            break
                
                prev1, prev2 = prev2, curr_match
    
    for match in matches:
        Match.objects.create(
            host_club_id=match[0],
            guest_club_id=match[1],
            date_time=match[2][0],
            stadium_id=match[3]
        )


@transaction.atomic()
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
            # logo=logos,
        )
        sample_clubs.append(sample_club)

    generate_matches(sample_clubs)

    return Response({'message': 'Successful!'})