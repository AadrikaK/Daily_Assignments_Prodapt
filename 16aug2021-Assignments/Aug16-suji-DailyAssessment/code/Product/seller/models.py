from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    sid=models.IntegerField()
    number=models.BigIntegerField()