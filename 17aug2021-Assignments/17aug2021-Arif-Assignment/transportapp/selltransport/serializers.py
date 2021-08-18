from rest_framework import serializers
from selltransport.models import Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','sprice','snum')