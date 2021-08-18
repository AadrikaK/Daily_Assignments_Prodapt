from django.db import models
from django.db import models

class Seller(models.Model):
    sname=models.CharField(max_length=50)
    sprice=models.IntegerField()
    snum=models.BigIntegerField()
