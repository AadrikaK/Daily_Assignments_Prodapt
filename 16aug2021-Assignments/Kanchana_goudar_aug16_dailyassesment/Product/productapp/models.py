from django.db import models

# Create your models here.
class Product(models.Model):
    pcode=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    des=models.CharField(max_length=50)
    price=models.IntegerField()
