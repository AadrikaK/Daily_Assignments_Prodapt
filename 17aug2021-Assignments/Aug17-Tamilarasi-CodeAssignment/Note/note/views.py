from note.models import Note
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from note.serializers import NoteSerializer
from note.models import Note
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
def myNoteDetails(request,title):
    try:
        notes=Note.objects.get(title=title)
        if (request.method=="GET"):    
            note_serializer=NoteSerializer(notes)
            return JsonResponse(note_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            notes.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            note_serialize=NoteSerializer(notes,data=dict)
            if(note_serialize.is_valid()):
                note_serialize.save()
                return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(note_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Note.DoesNotExist:
        return HttpResponse("Invalid Notes Title",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def myNoteList(request):
    if(request.method=="GET"):
        notes=Note.objects.all()
        note_serializer=NoteSerializer(notes,many=True)
        return JsonResponse(note_serializer.data,safe=False)

@csrf_exempt
def myNotePage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        note_serialize=NoteSerializer(data=dict)
        if(note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        