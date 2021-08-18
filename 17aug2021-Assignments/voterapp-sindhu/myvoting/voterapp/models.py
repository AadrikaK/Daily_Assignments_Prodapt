from django.db import models

# # Create your models here.
class Voterapp(models.Model):
    vid=models.IntegerField()
    vname=models.CharField(max_length=50)
    vaddress=models.CharField(max_length=50)
    vphoneno=models.BigIntegerField()