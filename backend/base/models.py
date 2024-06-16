from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SHORT_STRLEN = 10
SMALL_STRLEN = 25
STRLEN = 45
LONG_STRLEN = 125



class Season(models.Model):
    season_id = models.AutoField(primary_key=True, editable=False)
    cup_image_path = models.ImageField(upload_to='cups', max_length=STRLEN, null=True, blank=True)
    date = models.DateField(unique=True)
    kit1_id = models.OneToOneField(Kit, on_delete=models.CASCADE)
    kit2_id = models.OneToOneField(Kit, on_delete=models.CASCADE)
    kit3_id = models.OneToOneField(Kit, on_delete=models.CASCADE)
    kit4_id = models.OneToOneField(Kit, on_delete=models.CASCADE)

    # ...

    def __str__(self):
        return f'Seaseon {self.date.year}'
    

class Employee(models.Model):
    employee_id = models.OneToOneField(User, primary_key=True)
    image_path = models.ImageField(upload_to='employees', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    cv_path = models.FileField(upload_to='CVs')
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    gender = models.BooleanField()

    def __str__(self):
        return f'{self.employee_id}({self.position})'
    


class ClubStaff(models.Model):
    staff_id = models.OneToOneField(User, primary_key=True)
    image_path = models.ImageField(upload_to='club_staff', max_length=STRLEN, null=True, blank=True)
    birth_date = models.DateField()
    position = models.CharField(max_length=SMALL_STRLEN)
    description = models.TextField()
    club = models.models.ForeignKey(Club, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.staff_id}({self.position})'
    




