from django.db import models
from django.db.models import fields
from rest_framework import serializers
from vegitableapp.models import Vegitableapp1

class VegitableSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vegitableapp1
        fields = ('vegitableid','vegitablename','vegitabledescription','vegitableprice')