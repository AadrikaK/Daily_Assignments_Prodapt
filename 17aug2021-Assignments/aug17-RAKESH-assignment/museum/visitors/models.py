
from django.db import models

# Create your models here.
class Visitors(models.Model):
    name=models.CharField(max_length=100)
    ticketno=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phno=models.BigIntegerField()