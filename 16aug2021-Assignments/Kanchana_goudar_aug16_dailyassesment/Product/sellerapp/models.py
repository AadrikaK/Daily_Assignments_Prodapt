from django.db import models

# Create your models here.

class Seller(models.Model):
    Sid=models.CharField(max_length=50)
    Sname=models.CharField(max_length=50)
    Adress=models.CharField(max_length=50)
    Phno=models.IntegerField()

