from rest_framework import serializers
from SellerApp.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','sid','saddress','snum')