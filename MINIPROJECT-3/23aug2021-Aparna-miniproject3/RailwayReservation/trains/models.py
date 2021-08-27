from django.db import models

# Create your models here.
class Trains(models.Model):
    trainName = models.CharField(max_length=50, unique=True)
    trainNumber = models.CharField(max_length=20,unique=True)
    fromStation = models.CharField(max_length=40)
    toStation = models.CharField(max_length=40)
    runningDays = models.CharField(max_length=30)
