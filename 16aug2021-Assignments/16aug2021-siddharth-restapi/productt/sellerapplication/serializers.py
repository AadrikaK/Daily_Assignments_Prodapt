
from rest_framework import serializers
from sellerapplication.models import Seller

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','sid','sadd','sphone')