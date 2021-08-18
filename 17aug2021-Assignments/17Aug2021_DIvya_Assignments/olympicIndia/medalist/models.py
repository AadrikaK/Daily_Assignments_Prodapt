from django.db import models

# Create your models here.
class Medalist(models.Model):
    place = models.IntegerField()
    medal = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    