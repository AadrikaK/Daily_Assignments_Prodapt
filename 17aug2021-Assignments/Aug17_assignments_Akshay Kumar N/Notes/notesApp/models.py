from django.db import models

# Create your models here.

class Notes(models.Model):
    notesid = models.IntegerField()
    notestitle = models.CharField(max_length=50)
    notesdesc = models.CharField(max_length=50)
    notespages = models.IntegerField()
    
