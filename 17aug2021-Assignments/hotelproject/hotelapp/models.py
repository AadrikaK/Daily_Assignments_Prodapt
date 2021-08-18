from django.db import models

# Create your models here.

class hotel(models.Model):
    name=models.CharField(max_length=50)
    phno=models.IntegerField()
    adress=models.CharField(max_length=50)
    rno=models.BigIntegerField()
