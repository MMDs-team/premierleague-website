from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from base.models import Action, Club, Match, SampleClub, Season
from base.serializers.stats_serializers import SampleClubSerializer
from bisect import bisect_left, bisect_right
from django.db.models import Value, F

ACTION_NAMES = [
    'goal',
    'goal_from_header',
    'goal_from_penalty',
    'goal_from_freekick',
    'goal_from_inside_box',
    'goal_from_outside_box',
    'goal_from_counter_attack',
    'save',
    'own_goal',
    'shot',
    'pass',
    'cross',
    'offside',
    'yellow_card',
    'red_card',
    'tackle',
    'foul',
    'penalty',
    'corner '
]

ID_START = 1
ACTIONS = dict(zip(
    ACTION_NAMES, 
    range(ID_START, len(ACTION_NAMES) + 1)
))

# 2.5s
def count_matches(season, comp):
    current_season = Season.objects.latest('date').season_id
    sample_clubs = SampleClub.objects.filter(
            season=(season if season != -1 else current_season)
        ).values('club', 'sample_club_id')

    sample_clubs = [
        {'club': sample_club['club'], 'sample_club': sample_club['sample_club_id']}
        for sample_club in sample_clubs
    ]

    result = []
    for sample_club in sample_clubs:
        host_matches = Match.objects.filter(host_club=sample_club['sample_club'])
        guest_matches = Match.objects.filter(guest_club=sample_club['sample_club'])

        if season == -1:
            host_matches = Match.objects.select_related('host_club__club') \
                    .filter(host_club__club=sample_club['club'])

            guest_matches = Match.objects.select_related('guest_club__club') \
                    .filter(guest_club__club=sample_club['club'])
        
        host_matches = list(host_matches)
        guest_matches = list(guest_matches)

        count = 0
        for match in host_matches: 
            scores = tuple(int(score) for score in match.result.split('-'))
            count += comp(scores[0], scores[1])

        for match in guest_matches: 
            scores = tuple(int(score) for score in match.result.split('-'))
            count += comp(scores[1], scores[0])
        
        club = SampleClub.objects.get(pk=sample_club['sample_club'])
        serializer = SampleClubSerializer(club, many=False)

        result.append(dict(serializer.data) | {'count': count})

    return Response(result)


def count_actions(season, action_type, subject=True):
    curr_season = Season.objects.latest('date').season_id
    sample_clubs = SampleClub.objects.filter(
        season=(season if season != -1 else curr_season)
    ).order_by('club_id')

    result = sample_clubs.values('club_id', name=F('club__name'))

    sample_clubs = list(sample_clubs)
    for i in range(len(result)):
        result[i]['logo'] = sample_clubs[i].logo.url

    for res in result: res['count'] = 0

    clubs = [club['club_id'] for club in result]

    actions = None
    if subject: actions = Action.objects.filter(action_type=action_type).annotate(player_id=F('subject__player_user')) \
            .values('player_id', 'match_id', from_home=F('subject_from_home'))
    else: actions = Action.objects.filter(action_type=action_type) \
            .values('match_id', player_id=F('object_id'), from_home=Value(not F('subject_from_home')))

    actions = [action for action in actions.order_by('from_home')]
    for action in actions:
        match = Match.objects.get(pk=action['match_id'])
        curr_season = match.host_club.season_id if action['from_home'] else match.guest_club.season_id
        curr_club = match.host_club.club_id if action['from_home'] else match.guest_club.club_id

        if curr_season == season or season == -1:
            index = bisect_left(result, curr_club, key=lambda res: res['club_id'])
            if index < len(result): result[index]['count'] += 1
    
    for res in result: res.pop('club_id')

    return Response(result)


@api_view(['GET'])
def stats_top_club(request):
    action_type = request.GET['at']
    season = int(request.GET['se'])

    response = Response({})
    match action_type:
        case 'wins': response = count_matches(season, lambda self, other: self > other)
        case 'loses': response = count_matches(season, lambda self, other: self < other)
        case 'clean_sheets': response = count_matches(season, lambda self, other: other == 0)

        case 'goals': response = count_actions(season, action_type=ACTIONS['goal'])
        case 'yellow_cards': response = count_actions(season, action_type=ACTIONS['yellow_card'], subject=False)
        case 'red_cards': response = count_actions(season, action_type=ACTIONS['red_card'], subject=False)
        case 'shots': response = count_actions(season, action_type=ACTIONS['shot'])
        case 'goals_from_header': response = count_actions(season, action_type=ACTIONS['goal_from_header'])
        case 'goals_from_penalty': response = count_actions(season, action_type=ACTIONS['goal_from_penalty'])
        case 'goals_from_freekick': response = count_actions(season, action_type=ACTIONS['goal_from_freekick'])
        case 'goals_from_inside_box': response = count_actions(season, action_type=ACTIONS['goal_from_inside_box'])
        case 'goals_from_outside_box': response = count_actions(season, action_type=ACTIONS['goal_from_outside_box'])
        case 'goals_from_counter_attack': response = count_actions(season, action_type=ACTIONS['goal_from_counter_attack'])
        case 'offsides': response = count_actions(season, action_type=ACTIONS['offside'], subject=False)
        case 'saves': response = count_actions(season, action_type=ACTIONS['save'])
        case 'tackles': response = count_actions(season, action_type=ACTIONS['tackle'])
        case 'own_goals': response = count_actions(season, action_type=ACTIONS['own_goal'])
        case 'fouls': response = count_actions(season, action_type=ACTIONS['foul'])
        case 'penalties': response = count_actions(season, action_type=ACTIONS['penalty'])
        case 'passes': response = count_actions(season, action_type=ACTIONS['pass'])
        case 'crosses': response = count_actions(season, action_type=ACTIONS['cross'])
        case 'corners': response = count_actions(season, action_type=ACTIONS['corner'])
        case _: response = Response({
            'detail': f'There is no action type called {action_type}'
        })

    return response