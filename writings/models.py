from django.db import models
import datetime

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="writing/")
    date = models.DateField(datetime.date.today)
    