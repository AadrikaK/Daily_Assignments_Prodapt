from django.db import models
# Create your models here.
class Doctors(models.Model):
    dname=models.CharField(max_length=50)
    dadd=models.CharField(max_length=50)
    dmob=models.CharField(max_length=50)
    did=models.CharField(max_length=50)
    
