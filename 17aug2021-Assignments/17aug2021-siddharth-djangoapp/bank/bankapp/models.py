from django.db import models

class Banking(models.Model):
    
    code=models.IntegerField()
    name=models.CharField(max_length=50)
    desig=models.CharField(max_length=50)
    sal=models.IntegerField()


