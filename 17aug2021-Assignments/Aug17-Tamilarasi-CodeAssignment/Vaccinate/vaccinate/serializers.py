from rest_framework import serializers
from vaccinate.models import Vaccinate

class VaccinateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vaccinate
        fields=('vno','vname','vaddress','vaadharno','vmblno')
        