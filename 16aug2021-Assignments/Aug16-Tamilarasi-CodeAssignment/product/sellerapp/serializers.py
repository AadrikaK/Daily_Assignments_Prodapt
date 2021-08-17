from rest_framework import serializers
from sellerapp.models import Sellerapp

class SellerappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sellerapp
        fields=('sell_id','sell_name','sell_address','sell_mblno')
        