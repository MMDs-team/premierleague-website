from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125



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

    sponsers = models.ManyToManyField(
        'Sponser',
        through='SeaSpon',
        through_fields=('season', 'sponser')
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



