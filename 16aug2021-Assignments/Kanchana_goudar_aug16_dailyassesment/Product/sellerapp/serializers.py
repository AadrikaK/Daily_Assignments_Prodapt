from rest_framework import serializers
from sellerapp.models import Seller

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('Sid','Sname','Adress','Phno')