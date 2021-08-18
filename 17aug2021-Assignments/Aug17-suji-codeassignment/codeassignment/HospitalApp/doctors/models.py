from django.db import models

# Create your models here.
class Doctors(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    
