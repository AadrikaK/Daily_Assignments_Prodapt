from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=50)
    seller_ID = models.IntegerField()
    seller_add = models.CharField(max_length=50)
    seller_phno = models.IntegerField()