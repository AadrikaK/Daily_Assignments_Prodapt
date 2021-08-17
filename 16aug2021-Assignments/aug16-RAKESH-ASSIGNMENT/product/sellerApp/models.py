from django.db import models

# Create your models here.
class Seller(models.Model):
    # name=models.CharField(max_length=100,default='No NAME',blank=True)
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()
    address=models.CharField(max_length=150)
    phno=models.BigIntegerField()