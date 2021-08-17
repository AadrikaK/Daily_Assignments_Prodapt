from rest_framework import serializers
from sellerapp.models import Sellerapp

class SellerappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sellerapp
        fields=('sid','sname','saddress','sphonenum')
        
