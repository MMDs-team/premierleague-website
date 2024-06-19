from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

SEMESTERS = [('SUMMER', 'summer'), ('WINTER', 'winter')]
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125

class ActionType(models.Model) : 
    action_type_id = models.AutoField(primary_key=True, unique=True, editable=False)
    subtype = models.CharField(max_length=SMALL_STRLEN)
    type = models.CharField(max_length=SMALL_STRLEN)
    
    def __str__(self):
        return f'{self.type}-{self.subtype}'

class Refree(models.Model) : 
    refree = models.OneToOneField(User, primary_key=True, unique=True, editable=False, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='refrees', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    cv = models.FileField(upload_to='CVs')
    nationality = models.CharField(max_length=SMALL_STRLEN)
    
    def __str__(self):
        return f'{self.refree}'
    
class Player(models.Model) : 
    player = models.OneToOneField(User, primary_key=True, auto_Increment=True, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='players', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=SMALL_STRLEN)
    height = models.IntegerField()
    social_media = models.CharField(max_length=STRLEN, null=True, default='NULL')
    position = models.CharField(max_length=SMALL_STRLEN)
    heath_state = models.BooleanField(default=True)
    
    seasons = models.ManyToManyField(
        Season, 
        through='Transfer', 
        through_fields=('player', 'season')
    )   
    clubs = models.ManyToManyField(
        Club, 
        through='Transfer', 
        through_fields=('player', 'target_club', 'origin_club')
    )
        
    def __str__(self):
        return f'{self.player_id}-{self.position}'
    
class Action(models.Model) : 
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    subject = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    
    action_id = models.AutoField(primary_key=True, unique=True, editable=False)
    subject_from_home = models.BooleanField(null=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.action_id}-{self.time}'

class SamplePlayer(models.Model) : 
    player = models.ForeignKey(Player, primary_key=True, on_delete=models.CASCADE)
    club = models.ForeignKey(SampleClub, primary_key=True, on_delete=models.CASCADE)
    
    number_in_team = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    position = models.CharField(max_length=SMALL_STRLEN)
    
    def __str__(self):
        return f'{self.player}-{self.club}-{self.season}'

class Transfer(models.Model) : 
    player = models.ForeignKey(Player, primary_key=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, primary_key=True, on_delete=models.CASCADE)
    target_club = models.ForeignKey(Club, primary_key=True, on_delete=models.CASCADE)
    origin_club = models.ForeignKey(Club, null=True, on_delete=models.CASCADE)
    
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    semester = models.CharField(max_length=SMALL_STRLEN, default='SUMMER', choices=SEMESTER)
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.player}: {self.origin_club} -> {self.target_club}, {self.season}-{self.semester}'

class Match(models.Model) : 
    match_id = models.AutoField(primary_key=True, unique=True, editable=False)
    date_time = models.DateTimeField(auto_now_add=True)
    host_players = models.CharField(max_length=LONG_STRLEN, null=True, blank=True)
    away_players = models.CharField(max_length=LONG_STRLEN, null=True, blank=True)
    weather = models.CharField(max_length=SMALL_STRLEN, default='Stable')
    refree_kit_number = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)], null=True, blank=True)
    ticket_price = models.IntegerField()
    
    host_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE)
    guest_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    refree = models.ForeignKey(Refree, on_delete=models.CASCADE)
    first_refree_asist = models.ForeignKey(Refree, on_delete=models.CASCADE)
    second_refree_asist = models.ForeignKey(Refree, on_delete=models.CASCADE)
    fourth_official = models.ForeignKey(Refree, on_delete=models.CASCADE)
    
    match_spons = models.ManyToManyField(
        Sponsor, 
        through='MatchSpon', 
        through_fields=('match', 'player')
    )   
    casts = models.ManyToManyField(
        Broadcaster, 
        through='Casts', 
        through_fields=('match', 'broadcaster')
    )
    
    def __str__(self):
        return f'{self.match_id} -> {self.host_club} vs {self.guest_club}'