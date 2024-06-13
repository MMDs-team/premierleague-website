from django.db import models

# Create your models here.
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125

class ActionType(models.Model) : 
    action_type_id = models.IntegerField(primary_key=True, unique=True)
    subtype = models.CharField(max_length=SMALL_STRLEN, blank=False, null=False)
    type = models.CharField(max_length=SMALL_STRLEN, blank=False, null=False)
    

class Action(models.Model) : 
    '''
    action_id = 
    match_id =
    action_type_id = 
    subject_id = 
    object_id = 
    subject_from_home = 
    time = 
    '''

class Player(models.Model) : 
    '''
    player_id = 
    image_path = 
    birth_date = 
    nationality = 
    height = 
    social_media = 
    heath_state
    '''

class SamplePlayer(models.Model) : 
    '''
    player_id = 
    club_id = 
    season_id = 
    number_in_team = 
    position = 
    '''

class Transfer(models.Model) : 
    '''
    player_id = 
    season_id = 
    origin_club_id =
    target_club_id =
    date =
    amount =
    semester = 
    duration = 
    '''

class Refree(models.Model) : 
    '''
    refree_id =
    image_path = 
    birth_date =
    cv_path = 
    nationality =
    '''