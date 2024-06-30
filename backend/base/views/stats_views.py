from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from base.action_constants import ACTIONS
from bisect import bisect_left, bisect_right
from django.db.models import F, Value, Q
from django.db.models.aggregates import Count

from base.models import Action, Club, Match, Player, SampleClub, SamplePlayer, Season
from base.serializers.stats_serializers import *

RESULT_LEN = 10

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def stats_top_players_all_time(request):
    players = Player.objects.all()
    serializer = StatsTopPlayerAllTimeSerializer(players)
    return Response(serializer)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def stats_top_clubs_all_time(request):
    clubs = Club.objects.all()
    serializer = StatsTopClubAllTimeSerializer(clubs)
    return Response(serializer)


def count_club_matches(season, comp):
    current_season = Season.objects.latest('date').season_id
    sample_clubs = list(SampleClub.objects.filter(
            season=(season if season != -1 else current_season)
        ).values('club', sample_club=F('sample_club_id')))

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

        result.append(dict(serializer.data) | {'stats': count})

    result.sort(key=lambda x: x['stats'], reverse=True)
    return result


def count_club_actions(season, action_type, subject=True):
    curr_season = Season.objects.latest('date').season_id
    sample_clubs = SampleClub.objects.filter(
        season=(season if season != -1 else curr_season)
    ).order_by('club_id')

    result = sample_clubs.values('club_id', name=F('club__name'))

    sample_clubs = list(sample_clubs)
    for i in range(len(result)):
        result[i]['logo'] = sample_clubs[i].logo.url

    for res in result: res['stats'] = 0

    clubs = [club['club_id'] for club in result]

    actions = None
    if subject: actions = Action.objects.filter(action_type=action_type).annotate(player_id=F('subject__player_user')) \
            .values('player_id', 'match_id', from_home=F('subject_from_home'))
    else: actions = Action.objects.filter(action_type=action_type) \
            .values('match_id', player_id=F('object_id'), from_home=Value(not F('subject_from_home')))

    actions = [action for action in actions]
    for action in actions:
        match = Match.objects.get(pk=action['match_id'])
        curr_season = match.host_club.season_id if action['from_home'] else match.guest_club.season_id
        curr_club = match.host_club.club_id if action['from_home'] else match.guest_club.club_id

        if curr_season == season or season == -1:
            index = bisect_left(result, curr_club, key=lambda res: res['club_id'])
            if index < len(result): result[index]['stats'] += 1
    
    result = sorted(list(result), key=lambda x: x['stats'], reverse=True)
    return result


@api_view(['GET'])
def stats_top_club(request):
    season = int(request.GET['se'])
    action_type = request.GET['at']
    fr = int(request.GET['from'])
    order = request.GET.get('order', 'desc')

    response = {}
    match action_type:
        case 'wins': response = count_club_matches(season, lambda self, other: self > other)
        case 'loses': response = count_club_matches(season, lambda self, other: self < other)
        case 'clean_sheets': response = count_club_matches(season, lambda self, other: other == 0)

        case 'goals': response = count_club_actions(season, action_type=ACTIONS['goal'])
        case 'yellow_cards': response = count_club_actions(season, action_type=ACTIONS['yellow_card'], subject=False)
        case 'red_cards': response = count_club_actions(season, action_type=ACTIONS['red_card'], subject=False)
        case 'shots': response = count_club_actions(season, action_type=ACTIONS['shot'])
        case 'goals_from_header': response = count_club_actions(season, action_type=ACTIONS['goal_from_header'])
        case 'goals_from_penalty': response = count_club_actions(season, action_type=ACTIONS['goal_from_penalty'])
        case 'goals_from_freekick': response = count_club_actions(season, action_type=ACTIONS['goal_from_freekick'])
        case 'goals_from_inside_box': response = count_club_actions(season, action_type=ACTIONS['goal_from_inside_box'])
        case 'goals_from_outside_box': response = count_club_actions(season, action_type=ACTIONS['goal_from_outside_box'])
        case 'goals_from_counter_attack': response = count_club_actions(season, action_type=ACTIONS['goal_from_counter_attack'])
        case 'offsides': response = count_club_actions(season, action_type=ACTIONS['offside'], subject=False)
        case 'saves': response = count_club_actions(season, action_type=ACTIONS['save'])
        case 'tackles': response = count_club_actions(season, action_type=ACTIONS['tackle'])
        case 'own_goals': response = count_club_actions(season, action_type=ACTIONS['own_goal'])
        case 'fouls': response = count_club_actions(season, action_type=ACTIONS['foul'])
        case 'penalties': response = count_club_actions(season, action_type=ACTIONS['penalty'])
        case 'passes': response = count_club_actions(season, action_type=ACTIONS['pass'])
        case 'crosses': response = count_club_actions(season, action_type=ACTIONS['cross'])
        case 'corners': response = count_club_actions(season, action_type=ACTIONS['corner'])
        case _: response = {
            'detail': f'There is no action type called {action_type}'
        }
    
    
    if order == 'asc': response = response[-fr:-(fr + RESULT_LEN):-1]
    else: response = response[fr - 1:fr + RESULT_LEN - 1]

    return Response(response)

  
def count_player_actions(season, club, position, nationality, action_type, subject=True):
    actions = None
    if subject: actions = Action.objects.filter(action_type=action_type).annotate(player_id=F('subject__player_user')) \
            .values('player_id', 'match_id', from_home=F('subject_from_home'))
    else: actions = Action.objects.filter(action_type=action_type) \
            .values('match_id', player_id=F('object_id'), from_home=Value(not F('subject_from_home')))

    scores = {}
    actions = [action for action in actions]
    for action in actions:
        match = Match.objects.get(pk=action['match_id'])
        curr_season = match.host_club.season_id if action['from_home'] else match.guest_club.season_id
        curr_club = match.host_club.club_id if action['from_home'] else match.guest_club.club_id

        player = Player.objects.get(pk=action['player_id'])
        curr_position, curr_nationality = player.position, player.nationality

        if (curr_season == season or season == -1) and \
            (curr_club == club or club == -1) and \
            (curr_position == position or position == '-1') and \
            (curr_nationality == nationality or nationality == '-1'):
            scores[action['player_id']] = scores.get(action['player_id'], 0) + 1
    
    result = []
    current_season = Season.objects.latest('date').season_id
    for player_id, score in scores.items():
        sample_player = SamplePlayer.objects.filter(player=player_id).filter(club__season=current_season).first()
        if sample_player: 
            serializer = SamplePlayerSerializer(sample_player, many=False)
            result.append(dict(serializer.data) | {'player_id': player_id, 'stats': score})
        else:
            player = Player.objects.get(pk=player_id)
            serializer = PlayerSerializer(player)

            result.append(dict(serializer.data) | {'player_id': player_id, 'stats': score})
    
    result.sort(key=lambda x: x['stats'], reverse=True)

    return result


@api_view(['GET'])
def stats_top_player(request):
    season = int(request.GET['se'])
    club = int(request.GET['cl'])
    position = request.GET['po']
    nationality = request.GET['na']
    action_type = request.GET['at']
    fr = int(request.GET['from'])
    order = request.GET.get('order', 'desc')

    response = {}
    match action_type:
        case 'goals': 
            if position != 'GK': response = count_player_actions(season, club, position, nationality, ACTIONS['goal'])
            else: response = count_player_actions(season, club, position, nationality, ACTIONS['goal'], subject=False)
        
        case 'saves': response = count_player_actions(season, club, position, nationality, ACTIONS['save'])
        case 'assists': response = count_player_actions(season, club, position, nationality, ACTIONS['assist'])
        case 'appearances': response = count_player_actions(season, club, position, nationality, ACTIONS['appearance'])
        case 'yellow_cards': response = count_player_actions(season, club, position, nationality, ACTIONS['yellow_card'], subject=False)
        case 'red_cards': response = count_player_actions(season, club, position, nationality, ACTIONS['red_card'], subject=False)
        case 'shots': response = count_player_actions(season, club, position, nationality, ACTIONS['shot'])
        case 'goals_from_header': response = count_player_actions(season, club, position, nationality, ACTIONS['goal_from_header'])
        case 'goals_from_panalty': response = count_player_actions(season, club, position, nationality, ACTIONS['goal_from_penalty'])
        case 'goals_from_freekick': response = count_player_actions(season, club, position, nationality, ACTIONS['goal_from_freekick'])
        case 'offsides': response = count_player_actions(season, club, position, nationality, ACTIONS['offside'])
        case 'passes': response = count_player_actions(season, club, position, nationality, ACTIONS['pass'])
        case 'crosses': response = count_player_actions(season, club, position, nationality, ACTIONS['cross'])
        case 'corners': response = count_player_actions(season, club, position, nationality, ACTIONS['corner'])
        case 'tackles': response = count_player_actions(season, club, position, nationality, ACTIONS['tackle'])
        case 'own_goals': response = count_player_actions(season, club, position, nationality, ACTIONS['own_goal'])
        case 'clean_sheets': response = count_player_actions(season, club, position, nationality, ACTIONS['clean_sheet'])
        case 'penalties': 
            if position != 'GK': response = count_player_actions(season, club, position, nationality, ACTIONS['penalties'])
            else: 
                penalties = count_player_actions(season, club, position, nationality, ACTIONS['penalty'], subject=False)
                goals_from_penalty = count_player_actions(season, club, position, nationality, ACTIONS['goal_from_penalty'], subject=False)
                
                response = penalties
                goals_from_penalty.sort(key=lambda x: x['player_id'])
                for res in response:
                    index = bisect_left(goals_from_penalty, res['player_id'], key=lambda x: x['player_id'])
                    res['stats'] -= goals_from_penalty[index]['stats']

        case _: response = {
            'detail': f'There is no action type called {action_type}'
        }

    if len(response) != 0 and 'player_id' in response[0]:
        for res in response: del res['player_id']
    
    if order == 'asc': response = response[-fr:-(fr + RESULT_LEN):-1]
    else: response = response[fr - 1:fr + RESULT_LEN - 1]
    
    return Response(response)


def find_best_player(season, action_type, limit=-1):
    users = list(Action.objects.filter(Q(action_type=action_type) & Q(match_id__host_club__season=season)) \
        .values(user_id=F('subject_id')).annotate(count=Count('user_id')).order_by('-count'))
    
    if limit != -1: users = users[:limit]
    
    result = []
    for user in users:
        user_id = user['user_id']
        player_id = Player.objects.get(pk=user_id).player_id
        sample_player = SamplePlayer.objects.filter(Q(player=player_id) & Q(club__season=season)).first()

        if sample_player is None: continue
        serializer = SamplePlayerSerializerForTopPlayers(sample_player, many=False)
        result.append(dict(serializer.data) | {'stats': user['count']})
    
    return result


@api_view(['GET'])
def get_each_actions_best(request):
    current_season = Season.objects.latest('date').season_id
    player_actions = ['goal', 'assist', 'pass', 'clean_sheet']

    for_players = []
    for player_action in player_actions:
        for_players.append({'action_type': player_action})

        best_players = find_best_player(current_season, ACTIONS[player_action], limit=RESULT_LEN)
        for_players[-1]['players'] = best_players
    
    
    clubs = Club.objects.filter(sample_club_club__season=current_season)
    for_clubs = StatsOnClubs(clubs, current_season)

    tackles = list(count_club_actions(current_season, action_type=ACTIONS['tackle']))
    for tackle in tackles:
        club_id = tackle['club_id']
        main_stadium = clubs.get(pk=club_id).main_stadium_id

        tackle['main_stadium'] = main_stadium
    
    for_clubs['tackle'] = tackles
    result = {'player_stats': for_players, 'club_stats': for_clubs}

    return Response(result)