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
    name = models.CharField(max_length=STRLEN)
    image = models.ImageField(upload_to="clubs")
    description = models.TextField()
    est_date = models.DateField()
    website = models.URLField(max_length=LONG_STRLEN)
    social_media = models.URLField(max_length=LONG_STRLEN)
    email = models.EmailField(max_length=LONG_STRLEN)
    stadium = models.ForeignKey('ClubStad', null=True, blank=True, on_delete=models.SET_NULL, related_name='club_club_stad')

    sponsors = models.ManyToManyField(
        "Sponsor",
        through="ClubSpon",
        through_fields=("club", "sponsor")
    )
    
    stadiums = models.ManyToManyField(
        "Stadium",
        through="ClubStad",
        through_fields=("club", "stadium")
    )
    
    def __str__(self):
        return f"{self.club_id} - {self.name}"


class ClubStad(models.Model):
    club_stad_id = models.AutoField(primary_key=True, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_stad_club')
    stadium = models.ForeignKey("Stadium", models.CASCADE, related_name='club_stad_stadium')

    class Meta:
        unique_together = ['club', 'stadium']

    def __str__(self):
        return f"{self.club} - {self.stadium}"


class SampleClub(models.Model):
    sample_club_id = models.AutoField(primary_key=True, editable=False)
    logo = models.ImageField(upload_to="sample_clubs")
    total_points = models.PositiveIntegerField()

    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sample_club_club')
    season = models.ForeignKey("Season", on_delete=models.CASCADE, related_name='sample_club_season')

    players = models.ManyToManyField(
        "Player",
        through="SamplePlayer",
        through_fields=("club", "player")
    )

    class Meta:
        unique_together = ['club', 'season']

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
    club_spon_id = models.AutoField(primary_key=True, editable=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_spon_club')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='club_spon_sponsor')

    class Meta:
        unique_together = ['club', 'sponsor']

    def __str__(self):
        return f"{self.club} - {self.sponsor}"
    

class Kit(models.Model):
    kit_id = models.AutoField(primary_key=True, editable=False)
    image = models.ImageField(upload_to="kits")
    color = models.CharField(max_length=SHORT_STRLEN)

    sample_club = models.ForeignKey(SampleClub, null=True, blank=True, on_delete=models.CASCADE, related_name='kit_sample_club')

    def __str__(self):
        return f"{self.kit_id} - {self.sample_club}"


class MatchSpon(models.Model):
    match_spon_id = models.AutoField(primary_key=True, editable=False)
    amount = models.PositiveIntegerField()
    gif = models.FileField(upload_to="match_sponsors")

    match = models.ForeignKey("Match", on_delete=models.CASCADE, related_name='match_spon_match')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='match_spon_sponsor')

    class Meta:
        unique_together = ['match', 'sponsor']

    def __str__(self):
        return f"{self.match} - {self.sponsor}"


class SeaSpon(models.Model):
    sea_spon = models.AutoField(primary_key=True, editable=False)
    image = models.ImageField(upload_to="season_sponsors")
    amount = models.PositiveIntegerField()
    link = models.URLField(max_length=LONG_STRLEN)

    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sea_spon_sponsor')
    season = models.ForeignKey("Season", on_delete=models.CASCADE, related_name='sea_spon_season')

    class Meta:
        unique_together = ['season', 'sponsor']

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
    casts_id = models.AutoField(primary_key=True, editable=False)
    match = models.ForeignKey("Match", on_delete=models.CASCADE, related_name='casts_match')
    broadcaster = models.ForeignKey(Broadcaster, on_delete=models.CASCADE, related_name='casts_broadcaster')

    class Meta:
        unique_together = ['match', 'broadcaster']

    def __str__(self):
        return f"{self.match} - {self.broadcaster}"


class Season(models.Model):
    season_id = models.AutoField(primary_key=True, editable=False)
    cup_image = models.ImageField(upload_to='cups', max_length=STRLEN, null=True, blank=True)
    date = models.DateField(unique=True)
    kit1 = models.OneToOneField('Kit', on_delete=models.SET_NULL, null= True, blank=True, related_name='season_kit1')
    kit2 = models.OneToOneField('Kit', on_delete=models.SET_NULL, null= True, blank=True, related_name='season_kit2')
    kit3 = models.OneToOneField('Kit', on_delete=models.SET_NULL, null= True, blank=True, related_name='season_kit3')
    kit4 = models.OneToOneField('Kit', on_delete=models.SET_NULL, null= True, blank=True, related_name='season_kit4')

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
        return f'Season {self.date.year}'
    

class Employee(models.Model):
    employee = models.OneToOneField(User, primary_key=True, editable=False, on_delete=models.CASCADE, related_name='employee_user')
    image = models.ImageField(upload_to='employees', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    cv = models.FileField(upload_to='CVs')
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    gender = models.BooleanField()

    def __str__(self):
        return f'{self.employee}({self.position})'
    

class ClubStaff(models.Model):
    staff = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='club_staff_user')
    image = models.ImageField(upload_to='club_staff', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    club = models.ForeignKey('SampleClub', on_delete=models.CASCADE, related_name='club_staff_club')

    class Meta:
        unique_together = ['staff', 'club']

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
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='ticket_type_stadium')
    html_tag_id = models.CharField(max_length=SHORT_STRLEN)

    users = models.ManyToManyField(
        User,
        through='Ticket',
        through_fields=('type', 'user')
    )

    matches = models.ManyToManyField(
        'Match',
        through='Ticket',
        through_fields=('type', 'match')
    )

    def __str__(self):
        return f'Type{self.type_id}'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='ticket_user')
    match = models.ForeignKey("Match", on_delete=models.CASCADE, related_name='ticket_match')
    type = models.ForeignKey(TicketType, null=True, blank=True, on_delete=models.SET_NULL, related_name='ticket_type')
    seat_number = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        unique_together = ['user', 'match']

    def __str__(self):
        return f'Ticket({self.user}-{self.match})'


class ActionType(models.Model) : 
    action_type_id = models.AutoField(primary_key=True, unique=True, editable=False)
    subtype = models.CharField(max_length=SMALL_STRLEN)
    type = models.CharField(max_length=SMALL_STRLEN)
    
    def __str__(self):
        return f'{self.type}-{self.subtype}'


class Referee(models.Model) : 
    referee = models.OneToOneField(User, primary_key=True, unique=True, editable=False, on_delete=models.CASCADE, related_name='referee_user')
    
    image = models.ImageField(upload_to='referees', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    cv = models.FileField(upload_to='CVs')
    nationality = models.CharField(max_length=SMALL_STRLEN)

    def __str__(self):
        return f'{self.referee}'
    
    
class Player(models.Model) : 
    player = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='player_user')
    
    image = models.ImageField(upload_to='players', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=SMALL_STRLEN)
    height = models.IntegerField()
    social_media = models.CharField(max_length=STRLEN, null=True, default='NULL')
    position = models.CharField(max_length=SMALL_STRLEN)
    heath_state = models.BooleanField(default=True)
    
    sample_clubs = models.ManyToManyField(
        SampleClub, 
        through='Transfer', 
        through_fields=('player', 'target_club')
    )
        
    def __str__(self):
        return f'{self.player_id}-{self.position}'
    
    
class Action(models.Model) : 
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE, related_name='action_action_type')
    match = models.ForeignKey("Match", on_delete=models.CASCADE, related_name='action_match')
    subject = models.ForeignKey(User, on_delete=models.CASCADE, related_name='action_subject')
    object = models.ForeignKey(Player, null=True, on_delete=models.CASCADE, related_name='action_object')
    
    action_id = models.AutoField(primary_key=True, unique=True, editable=False)
    subject_from_home = models.BooleanField(null=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.action_id}-{self.time}'


class SamplePlayer(models.Model) : 
    sample_player_id = models.AutoField(primary_key=True, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sample_player_player')
    club = models.ForeignKey(SampleClub, on_delete=models.CASCADE, related_name='sample_player_club')
    
    number_in_team = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    position = models.CharField(max_length=SMALL_STRLEN)

    class Meta:
        unique_together = ['player', 'club']
    
    def __str__(self):
        return f'{self.player}-{self.club}-{self.season}'


class Transfer(models.Model) : 
    transfer_id = models.AutoField(primary_key=True, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='transfer_player')
    target_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE, related_name='transfer_target_club')
    origin_club = models.ForeignKey(SampleClub, null=True, on_delete=models.CASCADE, related_name='transfer_origin_club')
    
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    semester = models.CharField(max_length=SMALL_STRLEN, default='SUMMER', choices=SEMESTERS)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['player', 'target_club']
    
    def __str__(self):
        return f'{self.player}: {self.origin_club} -> {self.target_club}, {self.season}-{self.semester}'


class Match(models.Model) : 
    match_id = models.AutoField(primary_key=True, unique=True, editable=False)
    date_time = models.DateTimeField()
    host_players = models.CharField(max_length=LONG_STRLEN, null=True, blank=True)
    away_players = models.CharField(max_length=LONG_STRLEN, null=True, blank=True)
    weather = models.CharField(max_length=SMALL_STRLEN, default='Stable')
    referee_kit_number = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)], null=True, blank=True)
    ticket_price = models.IntegerField()
    resault = models.CharField(max_length=SMALL_STRLEN)
    
    host_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE, related_name='match_host_club')
    guest_club = models.ForeignKey(SampleClub, on_delete=models.CASCADE, related_name='match_guest_club')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='match_stadium')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='match_referee')
    first_referee_asist = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='match_first_referee_asist')
    second_referee_asist = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='match_second_referee_asist')
    fourth_official = models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='match_fourth_official')
    
    match_spons = models.ManyToManyField(
        Sponsor, 
        through='MatchSpon', 
        through_fields=('match', 'sponsor')
    )   
    casts = models.ManyToManyField(
        Broadcaster, 
        through='Casts', 
        through_fields=('match', 'broadcaster')
    )

    users = models.ManyToManyField(
        User,
        through='Ticket',
        through_fields=('match', 'user')
    )
    
    class Meta:
        unique_together = ['host_club', 'guest_club']

    def __str__(self):
        return f'{self.match_id} -> {self.host_club} vs {self.guest_club}'