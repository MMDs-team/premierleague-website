from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

SEMESTERS = [('SUMMER', 'summer'), ('WINTER', 'winter')]
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125

class Club(models.Model):
    club_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STR_LEN)
    image = models.ImageField(upload_to="clubs")
    description = models.TextField()
    est_date = models.DateField()
    website = models.URLField(max_length=LONG_STRLEN)
    social_media = models.URLField(max_length=LONG_STRLEN)
    email = models.Email.Field(max_length=LONG_STRLEN)

    sponsors = models.ManyToManyField(
        "Sponsor",
        through="ClubSpon",
        through_fields=("club", "sponsor")
    )
    
    stadiums = models.ManyToManyField(
        Stadium,
        through="ClubStad",
        through_fields=("club", "stadium")
    )

    seasons = models.ManyToManyField(
        Season, 
        through='Transfer', 
        through_fields=('target_club', 'origin_club', 'season')
    )

    
    def __str__(self):
        return f"{self.club_id} - {self.name}"


class ClubStad(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, models.CASCADE)

    # Discuss about how to add a delimiter related with season here!

    def __str__(self):
        return f"{self.club} - {self.stadium}"


class SampleClub(models.Model):
    logo = models.ImageField(upload_to="sample_clubs")
    total_points = models.PositiveIntegerField()

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    season = modesl.ForeignKey(Season, on_delete=models.CASCADE)

    players = models.ManyToManyField(
        Player,
        through="SamplePlayer",
        through_fields=("club", "player")
    )

    def __str__(self):
        return f"{self.club} - {self.season}"


class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STRLEN)
    logo = models.ImageField(upload_to="sponsors")
    website = models.URLField(max_length=LONG_STRLEN)

    def __str__(self):
        return f"{self.sponsor_id} - {self.name}"


class ClubSpon(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.club} - {self.sponsor}"
    

class Kit(models.Model):
    kit_id = models.AutoField(primary_key=True, editable=False)
    image = models.ImageField(upload_to="kits")
    color = models.CharField(max_length=SHORT_STRLEN)

    sample_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kit_id} - {self.sample_club}"


class MatchSpon(models.Model):
    amount = models.PositiveIntegerField()
    gif = models.FileField(upload_to="match_sponsors")

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.match} - {self.sponsor}"


class SeaSpon(models.Model):
    image = models.ImageField(upload_to="season_sponsors")
    amount = models.PositiveIntegerField()
    link = models.URLField(max_length=LONG_STRLEN)

    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.season} - {self.sponsor}"


class Broadcaster(models.Model):
    broadcaster_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STRLEN)

    s_date = models.DateField()
    e_date = models.DateField()

    def __str__(self):
        return f"{self.broadcaster} - {self.name}"


class Casts(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    broadcaster = models.ForeignKey(Broadcaster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.match} - {self.broadcaster}"


class Season(models.Model):
    season_id = models.AutoField(primary_key=True, editable=False)
    cup_image = models.ImageField(upload_to='cups', max_length=STRLEN, null=True, blank=True)
    date = models.DateField(unique=True)
    kit1 = models.OneToOneField('Kit')
    kit2 = models.OneToOneField('Kit')
    kit3 = models.OneToOneField('Kit')
    kit4 = models.OneToOneField('Kit')

    clubs = models.ManyToManyField(
        'Club',
        through='SampleClub',
        through_fields=('season', 'club')
    )

    sponsors = models.ManyToManyField(
        'Sponsor',
        through='SeaSpon',
        through_fields=('season', 'sponsor')
    )


    def __str__(self):
        return f'Seaseon {self.date.year}'
    

class Employee(models.Model):
    employee = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employees', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    cv_path = models.FileField(upload_to='CVs')
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    gender = models.BooleanField()

    def __str__(self):
        return f'{self.employee}({self.position})'
    


class ClubStaff(models.Model):
    staff = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='club_staff', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    club = models.ForeignKey('SampleClub', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.staff}({self.position})'
    




class Stadium(models.Model):
    stadium_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STRLEN)
    city = models.CharField(max_length=SMALL_STRLEN)
    image = models.ImageField(upload_to='stadiums')
    address = models.CharField(max_length=LONG_STRLEN)
    coordinates = models.CharField(max_length=STRLEN)
    capacity = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return str(self.name)



class TicketType(models.Model):
    type_id = models.AutoField(primary_key=True, editable=False)
    ratio = models.DecimalField(max_digits=4, decimal_places=2)
    s_number = models.IntegerField()
    e_number = models.IntegerField()
    color = models.CharField(max_length=SHORT_STRLEN)
    description = models.TextField(null=True, blank=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    html_tag_id = models.CharField(max_length=SHORT_STRLEN)

    def __str__(self):
        return f'Type{self.type_id}'
    



class Ticket(models.Model):
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, primary_key=True, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    type = models.ForeignKey(TicketType)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Ticket({self.user}-{self.match})'



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