from rest_framework import serializers
from sellerApp.models import Seller


class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','sid','address','phno')