from rest_framework import serializers
from Sellerapp.models import Seller

class Sellerserializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','sid','sadd','sphone')
