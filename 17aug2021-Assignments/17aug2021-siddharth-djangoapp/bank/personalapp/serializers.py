from rest_framework import serializers
from personalapp.models import Personal

class PersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Personal
        fields=('account','custname','place','bal')