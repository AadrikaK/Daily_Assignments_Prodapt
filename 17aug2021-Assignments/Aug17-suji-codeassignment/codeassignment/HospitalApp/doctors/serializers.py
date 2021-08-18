from django.db import models
from django.db.models import fields
from rest_framework import serializers
from doctors.models import Doctors

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields=('name','address','specialization')