from django.db import models

# Create your models here.

class Seller(models.Model):
    SellerName = models.CharField(max_length = 50)
    SellerID = models.IntegerField()
    SellerAdd = models.CharField(max_length = 50)
    SellerPhone = models.BigIntegerField()