from django.db import models

# Create your models here.
class Product(models.Model):
    # name=models.CharField(max_length=100,default='No NAME',blank=True)
    pname=models.CharField(max_length=100)
    pcode=models.IntegerField()
    description=models.CharField(max_length=150)
    price=models.IntegerField()
    
