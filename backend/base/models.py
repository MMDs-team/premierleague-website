from django.db import models

# Create your models here.
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125

"""
    TODO:
    -> Add keys.
"""

"""
group1: -> Khandan
Club
SampleClub
kit
Sponser
ClubSpon
MatchSpon
SeasonSpon
BroadCaster
Casts
"""

class Club(models.Model):
    club_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STR_LEN)
    image = models.ImageField(upload_to="clubs")
    description = models.TextField()
    est_date = models.DateField()
    website = models.URLField(max_length=LONG_STRLEN)
    social_media = models.URLField(max_length=LONG_STRLEN)
    email = models.Email.Field(max_length=LONG_STRLEN)


class SampleClub(models.Model):
    logo = models.ImageField(upload_to="sample_clubs")
    total_points = models.PositiveIntegerField()


class Kit(models.Model):
    kit_id = models.AutoField(primary_key=True, editable=False)
    image = models.ImageField(upload_to="kits")
    color = models.CharField(max_length=SHORT_STRLEN)


class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STRLEN)
    logo = models.ImageField(upload_to="sponsors")
    website = models.URLField(max_length=LONG_STRLEN)


class ClubSpon(models.Model):
    ...


class MatchSpon(models.Model):
    amount = models.PositiveIntegerField()
    gif = models.FileField(upload_to="match_sponsors")


class SeasonSpon(models.Model):
    image = models.ImageField(upload_to="season_sponsors")
    amount = models.PositiveIntegerField()
    link = models.URLField(max_length=LONG_STRLEN)


class Broadcaster(models.Model):
    broadcaster_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=STRLEN)

    s_date = models.DateField()
    e_date = models.DateField()


class Casts(models.Model):
    ...
