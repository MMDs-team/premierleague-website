from rest_framework import serializers
from base.models import SamplePlayer, Match, SampleClub, Club, Stadium
from django.utils import timezone

CLUB_POINT = dict()
CLUB_MATCH_COUNT = dict()
CLUB_GOAL_COUNT = dict()
CLUB_GOAL_CONCEDED_COUNT = dict()
CLUB_WIN_COUNT = dict()
CLUB_LOSE_COUNT = dict()
CLUB_DRWAN_COUNT = dict()
CLUB_LAST_MATCHES = dict()
CLUB_LOGO = dict()
SEASON_CLUBS = set()


class PlayersOverviewSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='player.player.first_name', read_only=True)
    last_name = serializers.CharField(source='player.player.last_name', read_only=True)
    nationality = serializers.CharField(source='player.nationality', read_only=True)
    image = serializers.FileField(source='player.image', read_only=True)

    class Meta:
        model = SamplePlayer
        fields = (
            'sample_player_id',
            'first_name',
            'last_name', 
            'position',
            'nationality',
            'image',
        )
        
        
class SeasonClubsOverviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = SampleClub
        fields = (
            'sample_club_id',
            'name',
            'logo',
        )
   
class AllClubsOverviewSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField(read_only=True)
    main_stadium = serializers.SerializerMethodField(read_only=True)
    
    def get_logo(self, obj):
        logo = SampleClub.objects.filter(club=obj.club_id).latest('season__date').logo
        return logo.url
    
    def get_main_stadium(self, obj):
        return obj.main_stadium.name
    
    class Meta:
        model = Club
        fields = (
            'club_id',
            'name',
            'logo',
            'main_stadium_id',
            'main_stadium',
        )
    

class SampleClubSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='club.name')
    class Meta:
        model = SampleClub
        fields = [
            'name',
            'logo'
        ]

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = [
            'name',
            'city'
        ]
        
class MatchSerializerForFixtures(serializers.ModelSerializer):
    time = serializers.SerializerMethodField(read_only=True)
    host_club = serializers.SerializerMethodField(read_only=True)
    guest_club = serializers.SerializerMethodField(read_only=True)
    stadium = serializers.SerializerMethodField(read_only=True)
    
    def get_time(self, obj):
        return obj.date_time.time()
    
    def get_host_club(self, obj):
        host_club = obj.host_club
        serializer = SampleClubSerializer(host_club, many=False)

        return serializer.data

    def get_guest_club(self, obj):
        guest_club = obj.guest_club
        serializer = SampleClubSerializer(guest_club, many=False)

        return serializer.data
    
    def get_stadium(self, obj):
        stadium = obj.stadium
        serializer = StadiumSerializer(stadium, many=False)
        
        return serializer.data
        
    class Meta:
        model = Match
        fields = [
            'match_id',
            'time',
            'ticket_price',
            'result',
            'host_club',
            'guest_club',
            'stadium'
        ]
        
############################ table ############################
        
def serializer_func(season) : 
    clubs = Club.objects.all()
    data = list()
    
    for obj in clubs : 
        if obj.club_id not in SEASON_CLUBS : continue
        
        club = dict()
        id = obj.club_id
        name = obj.name 
        
        club['club_id'] = id 
        club['name'] = name 
        club['logo'] = CLUB_LOGO.get(id, None) 
        club['played'] = CLUB_MATCH_COUNT.get(id, 0) 
        club['won'] = CLUB_WIN_COUNT.get(id, 0) 
        club['drawn'] = CLUB_DRWAN_COUNT.get(id, 0) 
        club['lost'] = CLUB_LOSE_COUNT.get(id, 0) 
        club['goal'] = CLUB_GOAL_COUNT.get(id, 0) 
        club['goal_conCeded'] = CLUB_GOAL_CONCEDED_COUNT.get(id, 0) 
        club['goal_difference'] = club['goal'] - club['goal_conCeded']
        club['point'] = CLUB_POINT.get(id, 0) 
        if season != -1:
            club['last_matches'] = []
            counter = 0
            for i in CLUB_LAST_MATCHES[id] :
                counter += 1
                club['last_matches'].append(i)
                if counter == 5 :
                    break
        
        data.append(club)
    return data 
       
def club_table_info(season, query, match_week, home_away) : 
    match_week = 100 if match_week == -1 else match_week
    for obj in query :
        
        now = timezone.now()
        if now < obj.date_time :
                break
            
        c1 = obj.host_club.club.club_id
        c2 = obj.guest_club.club.club_id
        
        SEASON_CLUBS.add(c1)
        SEASON_CLUBS.add(c2)
        
        CLUB_LOGO[c1] = obj.host_club.logo.url
        CLUB_LOGO[c2] = obj.guest_club.logo.url
        
        res = obj.result
        g1 = int(res[:res.index('-')])
        g2 = int(res[res.index('-') + 1:])
        
        if season != -1 :
            if c1 not in CLUB_LAST_MATCHES : 
                CLUB_LAST_MATCHES[c1] = []
            if c2 not in CLUB_LAST_MATCHES : 
                CLUB_LAST_MATCHES[c2] = []
            CLUB_LAST_MATCHES[c1].append([c1, obj.host_club.club.name, CLUB_LOGO[c1], c2, obj.guest_club.club.name, CLUB_LOGO[c2], res])
            CLUB_LAST_MATCHES[c2].append([c1, obj.host_club.club.name, CLUB_LOGO[c1], c2, obj.guest_club.club.name, CLUB_LOGO[c2], res])
        
        CLUB_MATCH_COUNT[c1] = CLUB_MATCH_COUNT.get(c1, 0) + 1
        CLUB_MATCH_COUNT[c2] = CLUB_MATCH_COUNT.get(c2, 0) + 1  
        
        if CLUB_MATCH_COUNT[c1] > match_week : 
            continue
        if home_away == "H" or home_away == -1 : 
            CLUB_GOAL_COUNT[c1] = CLUB_GOAL_COUNT.get(c1, 0) + g1
            CLUB_GOAL_CONCEDED_COUNT[c1] = CLUB_GOAL_CONCEDED_COUNT.get(c1, 0) + g2  
            if g1 > g2 : 
                CLUB_WIN_COUNT[c1] = CLUB_WIN_COUNT.get(c1, 0) + 1
                CLUB_POINT[c1] = CLUB_POINT.get(c1, 0) + 3
            elif g1 < g2 : 
                CLUB_LOSE_COUNT[c1] = CLUB_LOSE_COUNT.get(c1, 0) + 1
            else :
                now = timezone.now()
                if now >= obj.date_time :
                    CLUB_DRWAN_COUNT[c1] = CLUB_DRWAN_COUNT.get(c1, 0) + 1
                    CLUB_POINT[c1] = CLUB_POINT.get(c1, 0) + 1
            
        if home_away == "A" or home_away == -1 : 
            CLUB_GOAL_COUNT[c2] = CLUB_GOAL_COUNT.get(c2, 0) + g2
            CLUB_GOAL_CONCEDED_COUNT[c2] = CLUB_GOAL_CONCEDED_COUNT.get(c2, 0) + g1  
            if g1 > g2 : 
                CLUB_LOSE_COUNT[c2] = CLUB_LOSE_COUNT.get(c2, 0) + 1
            elif g1 < g2 : 
                CLUB_POINT[c2] = CLUB_POINT.get(c2, 0) + 3
                CLUB_WIN_COUNT[c2] = CLUB_WIN_COUNT.get(c2, 0) + 1
            else :
                now = timezone.now()
                if now >= obj.date_time :
                    CLUB_DRWAN_COUNT[c2] = CLUB_DRWAN_COUNT.get(c2, 0) + 1
                    CLUB_POINT[c2] = CLUB_POINT.get(c2, 0) + 1
                    
    return serializer_func(season)

def table_serializer(request) : 
    matches = Match.objects.all()
    season = int(request.GET.get('se'))
    match_week = int(request.GET.get('mw'))
    home_away = int(request.GET.get('ha'))
    
    if season != -1: 
        matches = matches.filter(host_club__season__season_id=season)
    if match_week != -1: 
        matches = list(matches.order_by('-date_time'))
    matches = list(matches)
    data = sorted(club_table_info(season, matches, match_week, home_away), key=lambda x: (x['point'], x['goal_difference']), reverse=True)
    return data 