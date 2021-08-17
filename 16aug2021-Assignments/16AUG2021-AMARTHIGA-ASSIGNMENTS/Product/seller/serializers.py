from django.db.models import fields
from rest_framework import serializers
from seller.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('SellerName', 'SellerID', 'SellerAdd', 'SellerPhone')
        