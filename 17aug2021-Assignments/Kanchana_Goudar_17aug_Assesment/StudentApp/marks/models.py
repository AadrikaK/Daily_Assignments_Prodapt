from django.db import models

# Create your models here.
class Marks(models.Model):
    sub=models.CharField(max_length=50)
    score=models.IntegerField()
