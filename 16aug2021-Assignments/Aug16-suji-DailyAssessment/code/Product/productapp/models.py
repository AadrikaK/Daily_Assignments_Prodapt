from django.db import models

# Create your models here.
class Product1(models.Model):
    pname=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    code=models.IntegerField()
    price=models.IntegerField()