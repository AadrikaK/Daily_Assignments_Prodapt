from django.db.models import fields
from rest_framework import serializers
from starconstellation.models import Star


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ('star_name', 'star_shape', 'constel_family')
