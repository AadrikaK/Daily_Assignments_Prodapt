
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from sellerapp.models import sellersdata

class seller_Serializer(serializers.ModelSerializer):
    class Meta:
        model= sellersdata
        fields = ('seller_name','seller_id','seller_address','seller_phoneno')