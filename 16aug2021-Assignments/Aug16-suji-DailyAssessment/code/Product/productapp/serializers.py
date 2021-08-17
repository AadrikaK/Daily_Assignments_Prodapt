from django.db import models
from django.db.models import fields
from rest_framework import serializers
from productapp.models import Product1

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product1
        fields=('pname','description','code','price')