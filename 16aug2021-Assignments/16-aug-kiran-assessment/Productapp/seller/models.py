from django.db import models

# Create your models here.
class Seller(models.Model):
    sname=models.CharField(max_length=50)
    seller_id=models.IntegerField()
    address=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()