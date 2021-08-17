from django.db import models

# # Create your models here.
class Sellerapp(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=50)
    saddress=models.CharField(max_length=50)
    sphonenum=models.BigIntegerField(default=1)