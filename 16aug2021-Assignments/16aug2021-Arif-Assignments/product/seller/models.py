from django.db import models
class Seller(models.Model):
    name=models.CharField(max_length=50)
    scode=models.IntegerField()
    sadd=models.CharField(max_length=25)
    snum=models.BigIntegerField()

