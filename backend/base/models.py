from django.db import models

# Create your models here.

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
    return f"{club} - {sponsor}"
    

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
