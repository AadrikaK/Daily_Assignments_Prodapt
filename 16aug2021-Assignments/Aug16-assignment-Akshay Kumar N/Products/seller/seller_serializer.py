from seller.models import Sellers
from rest_framework import serializers
from seller.models import Sellers

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = ('sellerid','sellername','selleraddress','sellerphno')  