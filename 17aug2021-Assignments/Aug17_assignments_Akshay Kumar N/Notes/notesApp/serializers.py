
from rest_framework import serializers
from notesApp.models import Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('notesid','notestitle','notesdesc','notespages')