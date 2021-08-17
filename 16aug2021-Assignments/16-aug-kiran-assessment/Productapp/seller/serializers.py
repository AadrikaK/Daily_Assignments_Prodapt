from rest_framework import serializers
from seller.models import Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','seller_id','address','mobileno')