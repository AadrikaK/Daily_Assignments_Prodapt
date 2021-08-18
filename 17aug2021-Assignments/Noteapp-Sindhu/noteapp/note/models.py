from django.db import models

# # Create your models here.
class Note(models.Model):
    ntitle=models.CharField(max_length=50)
    ndescription=models.CharField(max_length=50)
    