from rest_framework import serializers
from base.models import Player, Action, SampleClub, SamplePlayer, Season
from base.action_constants import ACTIONS

APPEARANCE_ACTION_TYPE_ID = ACTIONS['appearance']
GOAL_ACTION_TYPE_ID = ACTIONS['goal']
ASSIST_ACTION_TYPE_ID = ACTIONS['assist']
CLEAN_SHEET_ACTION_TYPE_ID = ACTIONS['clean_sheet']
LAST_SEASON = None
PLAYER_CLUB_LOGO = dict()

class StatusTopPlayerAppearanceAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    appearances = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_appearances(self, obj):
        return Action.objects.filter(subject=obj.player, action_type=APPEARANCE_ACTION_TYPE_ID).count()
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'first_name',
            'username', 
            'image',
            'club_logo',
            'appearances',
        )
        
        
class StatusTopPlayerGoalAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    goal = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_goal(self, obj):
        return Action.objects.filter(subject=obj.player, action_type=GOAL_ACTION_TYPE_ID).count()
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'first_name',
            'username', 
            'image',
            'club_logo',
            'goal',
        )
        
        
class StatusTopPlayerAssistAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    assist = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_assist(self, obj):
        return Action.objects.filter(subject=obj.player, action_type=ASSIST_ACTION_TYPE_ID).count()
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'first_name',
            'username', 
            'image',
            'club_logo',
            'assist',
        )
        
        
class StatusTopGKCleanSeetAllTimeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.first_name', read_only=True)
    username = serializers.CharField(source='player.username', read_only=True)
    clean_sheet = serializers.SerializerMethodField(read_only=True)
    club_logo = serializers.SerializerMethodField(read_only=True)
    
    def get_clean_sheet(self, obj):
        return Action.objects.filter(subject=obj.player, action_type=CLEAN_SHEET_ACTION_TYPE_ID).count()
    
    def get_club_logo(self, obj):
        return PLAYER_CLUB_LOGO[obj]
        
    class Meta:
        model = Player
        fields = (
            'first_name',
            'username', 
            'image',
            'club_logo',
            'clean_sheet',
        )
        

def last_season() :
    global LAST_SEASON
    LAST_SEASON = Season.objects.all().latest('season_id').season_id


def player_logo(query) :
    for obj in query :
        try :
            last_club = SamplePlayer.objects.filter(player=obj.player_id).latest('player').club.sample_club_id
            logo = SampleClub.objects.filter(sample_club_id=last_club).first().logo.url
            PLAYER_CLUB_LOGO[obj] = logo
        except: 
            PLAYER_CLUB_LOGO[obj] = None
        
        
def StatusTopPlayerAllTimeSerializer(query) :
    last_season()
    player_logo(query)
    data = dict()
    
    data['appearance'] = sorted(StatusTopPlayerAppearanceAllTimeSerializer(query, many=True).data, key=lambda x: x['appearances'], reverse=True)
    data['goal']  = sorted(StatusTopPlayerGoalAllTimeSerializer(query, many=True).data, key=lambda x: x['goal'], reverse=True)
    data['assist']  = sorted(StatusTopPlayerAssistAllTimeSerializer(query, many=True).data, key=lambda x: x['assist'], reverse=True)
    gk = query.filter(position='GK')
    data['clean_sheet']  = sorted(StatusTopGKCleanSeetAllTimeSerializer(gk, many=True).data, key=lambda x: x['clean_sheet'], reverse=True)
    return data
  
  
class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = ['name', 'logo']


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