from django.db.models import fields
from rest_framework import serializers
from medalist.models import Medalist

class MedalistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medalist
        fields=('place','medal','game','name')