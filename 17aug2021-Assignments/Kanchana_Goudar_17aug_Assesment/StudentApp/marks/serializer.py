from rest_framework import serializers
from marks.models import Marks

class MarksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Marks
        fields=('sub','score')