from django.db import models
from django.db import models

class Transport(models.Model):
    tname=models.CharField(max_length=50)
    tprice=models.IntegerField()
