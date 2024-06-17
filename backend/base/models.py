from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

SEMESTER = [('SUMMER', 'summer'), ('WINTER', 'winter')]
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
    

class Action(models.Model) : 
    action_id = models.AutoField(primary_key=True, unique=True, editable=False)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    subject = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    subject_from_home = models.BooleanField(null=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.action_id}-{self.time}'

class Player(models.Model) : 
    player = models.OneToOneField(User, primary_key=True, auto_Increment=True, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='player', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=SMALL_STRLEN)
    height = models.IntegerField()
    social_media = models.CharField(max_length=STRLEN, null=True, default='NULL')
    position = models.CharField(max_length=SMALL_STRLEN) # add
    heath_state = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.player_id}-{self.position}'

class SamplePlayer(models.Model) : 
    player = models.ForeignKey(Player, primary_key=True, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, primary_key=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, primary_key=True, on_delete=models.CASCADE)
    number_in_team = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
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
    semester = models.CharField(max_length=SMALL_STRLEN, default="SUMMER", choices=SEMESTER)
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.player}: {self.origin_club} -> {self.target_club}, {self.season}-{self.semester}'

class Refree(models.Model) : 
    refree = models.OneToOneField(User, primary_key=True, unique=True, editable=False, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to='refree', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    cv_path = models.FileField(upload_to='CVs')
    nationality = models.CharField(max_length=SMALL_STRLEN)
    
    def __str__(self):
        return f'{self.refree}'