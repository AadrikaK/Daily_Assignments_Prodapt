from django.db import models

# Create your models here.
class Notes(models.Model):
    NoteTitle= models.CharField(max_length = 50)
    NoteDescri= models.CharField(max_length = 50)
