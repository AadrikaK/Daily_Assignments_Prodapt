from django.db import models

# Create your models here.

class Seller(models.Model):
    sname=models.CharField(max_length=50)
    sid=models.IntegerField()
    saddress=models.CharField(max_length=50)
    snum=models.BigIntegerField()