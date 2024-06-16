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
        return "Seaseon" + self.date.year
    
