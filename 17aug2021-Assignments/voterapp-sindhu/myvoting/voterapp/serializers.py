from rest_framework import serializers
from voterapp.models import Voterapp

class VoterappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Voterapp
        fields=('vid','vname','vaddress','vphoneno')