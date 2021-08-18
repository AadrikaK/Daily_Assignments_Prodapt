from django.db import models

# Create your models here.
class Vaccinate(models.Model):
    vno=models.IntegerField()
    vname=models.CharField(max_length=50)
    vaddress=models.CharField(max_length=50)
    vaadharno=models.BigIntegerField()
    vmblno=models.BigIntegerField()