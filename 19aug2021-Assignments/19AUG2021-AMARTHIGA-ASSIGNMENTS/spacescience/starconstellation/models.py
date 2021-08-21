from django.db import models

# Create your models here.
class Star(models.Model):
    star_name = models.CharField(max_length=25)
    star_shape = models.CharField(max_length=25)
    constel_family = models.CharField(max_length=50)


