from rest_framework import serializers
from base.models import Player, Action, SampleClub, SamplePlayer, Season, Match, Club
from base.action_constants import ACTIONS

APPEARANCE_ACTION_TYPE_ID = ACTIONS['appearance']
GOAL_ACTION_TYPE_ID = ACTIONS['goal']
ASSIST_ACTION_TYPE_ID = ACTIONS['assist']
CLEAN_SHEET_ACTION_TYPE_ID = ACTIONS['clean_sheet']
LAST_SEASON = None

PLAYER_CLUB_LOGO = dict()
CLUB_LOGO = dict()

APPEARANCE_COUNT_PLAYER = dict()
GOAL_COUNT_PLAYER = dict()
ASSIST_COUNT_PLAYER = dict()
CLEAN_SHEET_COUNT_PLAYER = dict()

LOSE_COUNT_CLUB = dict()
WIN_COUNT_CLUB = dict()
GOAL_COUNT_CLUB = dict()
GOAL_CONCEDED_COUNT_CLUB = dict()

########################## player stats #############################

class StatsTopPlayerAppearanceAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    appearances = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_appearances(self, obj):
        return APPEARANCE_COUNT_PLAYER.get(obj.player.id, 0)
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'player',
            'first_name',
            'username', 
            'image',
            'club_logo',
            'appearances',
        )
        
        
class StatsTopPlayerGoalAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    goal = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_goal(self, obj):
        return GOAL_COUNT_PLAYER.get(obj.player.id, 0)
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'player',
            'first_name',
            'username', 
            'image',
            'club_logo',
            'goal',
        )
        
        
class StatsTopPlayerAssistAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    assist = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_assist(self, obj):
        return ASSIST_COUNT_PLAYER.get(obj.player.id, 0)
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'player',
            'first_name',
            'username', 
            'image',
            'club_logo',
            'assist',
        )
        
        
class StatsTopGKCleanSeetAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    clean_sheet = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_clean_sheet(self, obj):
        return CLEAN_SHEET_COUNT_PLAYER.get(obj.player.id, 0)
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'player',
            'first_name',
            'username', 
            'image',
            'club_logo',
            'clean_sheet',
        )
        

def last_season() :
    global LAST_SEASON
    LAST_SEASON = Season.objects.all().latest('season_id').season_id
    
    
def player_info() : 
    actions = Action.objects.filter(match__host_club__season__season_id=LAST_SEASON)
    for obj in actions :
        player = obj.subject.id
        action_type = obj.action_type.action_type_id

        if action_type == APPEARANCE_ACTION_TYPE_ID :
            APPEARANCE_COUNT_PLAYER[player] = APPEARANCE_COUNT_PLAYER.get(player, 0) + 1
        
        elif action_type == GOAL_ACTION_TYPE_ID :
            GOAL_COUNT_PLAYER[player] = GOAL_COUNT_PLAYER.get(player, 0) + 1
            
        elif action_type == ASSIST_ACTION_TYPE_ID :
            ASSIST_COUNT_PLAYER[player] = ASSIST_COUNT_PLAYER.get(player, 0) + 1
            
        elif action_type == CLEAN_SHEET_ACTION_TYPE_ID :
            CLEAN_SHEET_COUNT_PLAYER[player] = CLEAN_SHEET_COUNT_PLAYER.get(player, 0) + 1    


def player_logo(query) :
    for obj in query :
        try :
            last_club = SamplePlayer.objects.filter(player=obj.player_id).latest('player').club.sample_club_id
            logo = SampleClub.objects.filter(sample_club_id=last_club).first().logo.url
            PLAYER_CLUB_LOGO[obj] = logo
        except: 
            PLAYER_CLUB_LOGO[obj] = None
        
        
def StatsTopPlayerAllTimeSerializer(query) :
    last_season()
    PLAYER_CLUB_LOGO.clear()
    player_logo(query)
    player_info()
    data = dict()

    data['appearance'] = sorted(StatsTopPlayerAppearanceAllTimeSerializer(query, many=True).data, key=lambda x: x['appearances'], reverse=True)[:10]
    data['goal']  = sorted(StatsTopPlayerGoalAllTimeSerializer(query, many=True).data, key=lambda x: x['goal'], reverse=True)[:10]
    data['assist']  = sorted(StatsTopPlayerAssistAllTimeSerializer(query, many=True).data, key=lambda x: x['assist'], reverse=True)[:10]
    gk = query.filter(position='GK')
    data['clean_sheet']  = sorted(StatsTopGKCleanSeetAllTimeSerializer(gk, many=True).data, key=lambda x: x['clean_sheet'], reverse=True)[:10]
    return data

########################## club stats #############################
 
class StatsTopClubWinAllTimeSerializer(serializers.ModelSerializer):
    win = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    main_stadium_name = serializers.CharField(source='main_stadium.name', read_only=True)
    
    def get_win(self, obj):
        return WIN_COUNT_CLUB.get(obj.club_id, 0)
    
    def get_club_logo(self, obj):
        return CLUB_LOGO[obj.club_id]
        
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'main_stadium', 
            'main_stadium_name',
            'club_logo',
            'win',
        )
        
        
class StatsTopClubLoseAllTimeSerializer(serializers.ModelSerializer):
    lose = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    main_stadium_name = serializers.CharField(source='main_stadium.name', read_only=True)
    
    def get_lose(self, obj):
        return LOSE_COUNT_CLUB.get(obj.club_id, 0)
    
    def get_club_logo(self, obj):
        return CLUB_LOGO[obj.club_id]
        
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'main_stadium', 
            'main_stadium_name', 
            'club_logo',
            'lose',
        )
       
        
class StatsTopClubGoalAllTimeSerializer(serializers.ModelSerializer):
    goal = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    main_stadium_name = serializers.CharField(source='main_stadium.name', read_only=True)
    
    def get_goal(self, obj):
        return GOAL_COUNT_CLUB.get(obj.club_id, 0)
    
    def get_club_logo(self, obj):
        return CLUB_LOGO[obj.club_id]
        
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'main_stadium', 
            'main_stadium_name', 
            'club_logo',
            'goal',
        )
        

class StatsTopClubGoalConcededAllTimeSerializer(serializers.ModelSerializer):
    goal_conceded = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_goal_conceded(self, obj):
        return GOAL_CONCEDED_COUNT_CLUB.get(obj.club_id, 0)
    
    def get_club_logo(self, obj):
        return CLUB_LOGO[obj.club_id]
        
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'main_stadium', 
            'club_logo',
            'goal_conceded',
        )
    
        
def club_info(season=-1) : 
    matchs = Match.objects.all()
    if season != -1: matchs = matchs.filter(host_club__season=season)
    for obj in matchs :
        c1 = obj.host_club.club.club_id
        c2 = obj.guest_club.club.club_id
        res = obj.result
        g1 = int(res[:res.index('-')])
        g2 = int(res[res.index('-') + 1:])

        GOAL_COUNT_CLUB[c1] = GOAL_COUNT_CLUB.get(c1, 0) + g1
        GOAL_COUNT_CLUB[c2] = GOAL_COUNT_CLUB.get(c2, 0) + g2
        GOAL_CONCEDED_COUNT_CLUB[c1] = GOAL_CONCEDED_COUNT_CLUB.get(c1, 0) + g2
        GOAL_CONCEDED_COUNT_CLUB[c2] = GOAL_CONCEDED_COUNT_CLUB.get(c2, 0) + g1
        
        if g1 > g2 :
            WIN_COUNT_CLUB[c1] = WIN_COUNT_CLUB.get(c1, 0) + 1
            LOSE_COUNT_CLUB[c2] = LOSE_COUNT_CLUB.get(c2, 0) + 1
        elif g1 < g2 :
            WIN_COUNT_CLUB[c2] = WIN_COUNT_CLUB.get(c2, 0) + 1
            LOSE_COUNT_CLUB[c1] = LOSE_COUNT_CLUB.get(c1, 0) + 1

        
def club_logo(query) :
    for obj in query :
        logo = SampleClub.objects.filter(club=obj.club_id).latest('season').logo.url
        CLUB_LOGO[obj.club_id] = logo
        
        
def StatsTopClubAllTimeSerializer(query) :
    club_logo(query)
    club_info()
    data = dict()
    data['win'] = sorted(StatsTopClubWinAllTimeSerializer(query, many=True).data, key=lambda x: x['win'], reverse=True)[:10]
    data['lose']  = sorted(StatsTopClubLoseAllTimeSerializer(query, many=True).data, key=lambda x: x['lose'], reverse=True)[:10]
    data['goal']  = sorted(StatsTopClubGoalAllTimeSerializer(query, many=True).data, key=lambda x: x['goal'], reverse=True)[:10]
    data['goal_conceded']  = sorted(StatsTopClubGoalConcededAllTimeSerializer(query, many=True).data, key=lambda x: x['goal_conceded'], reverse=True)[:10]
    return data

########################## stat base season #############################

class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = ['name', 'logo']


class SamplePlayerSerializerForTopPlayers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    sample_club = serializers.SerializerMethodField(read_only=True)

    def get_image(self, obj):
        image = obj.player.image

        return image.url

    def get_sample_club(self, obj):
        sample_club = obj.club
        serializer = SampleClubSerializer(sample_club, many=False)

        return serializer.data

    class Meta:
        model = SamplePlayer
        fields = [
            'first_name',
            'last_name',
            'image',
            'sample_club',
            'number_in_team'
        ]


class SamplePlayerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    position = serializers.CharField(source='player.position', read_only=True)
    sample_club = serializers.SerializerMethodField(read_only=True)
    nationality = serializers.CharField(source='player.nationality')

    def get_sample_club(self, obj):
        sample_club = obj.club
        serializer = SampleClubSerializer(sample_club, many=False)

        return serializer.data

    class Meta:
        model = SamplePlayer
        fields = [
            'first_name',
            'last_name',
            'sample_club',
            'position',
            'nationality'
        ]

        
class PlayerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.last_name', read_only=True)

    class Meta:
        model = Player
        fields = [
            'first_name',
            'last_name',
            'position',
            'nationality'
        ]


def StatsOnClubs(query, season) :
    CLUB_LOGO.clear()
    WIN_COUNT_CLUB.clear()
    LOSE_COUNT_CLUB.clear()
    GOAL_COUNT_CLUB.clear()
    
    club_logo(query)
    club_info(season)
    data = dict()
    data['win'] = sorted(StatsTopClubWinAllTimeSerializer(query, many=True).data, key=lambda x: x['win'], reverse=True)[:10]
    data['lose']  = sorted(StatsTopClubLoseAllTimeSerializer(query, many=True).data, key=lambda x: x['lose'], reverse=True)[:10]
    data['goal']  = sorted(StatsTopClubGoalAllTimeSerializer(query, many=True).data, key=lambda x: x['goal'], reverse=True)[:10]
    return data