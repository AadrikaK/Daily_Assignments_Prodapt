from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#import json
from notes.serializer import NotesSerializer
from notes.models import Notes 
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def addnote(request):
    if (request.method == 'POST'):
        mydata = JSONParser().parse(request)
        note_serialize = NotesSerializer(data=mydata)
        if(note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse("Serialization Error", status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse('Hi, Welcome to the Notes App')

@csrf_exempt
def viewnote(request):
    if (request.method =='GET'):
        notes = Notes.objects.all()
        note_serializers = NotesSerializer(notes, many=True )
        return JsonResponse(note_serializers.data, safe=False)

@csrf_exempt
def notes_details(request, id):
    try: 
        notes = Notes.objects.get(id=id)
        if (request.method == 'GET'):
            notes_serializer = NotesSerializer(notes)
            return JsonResponse(notes_serializer.data, safe = False, status=status.HTTP_200_OK)

        if (request.method == "DELETE"):
                    notes.delete()
                    return HttpResponse("The field has been deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             mydata = JSONParser().parse(request)
             note_serialize = NotesSerializer(notes, data=mydata)
             if(note_serialize.is_valid()):
                 note_serialize.save()
                 return JsonResponse(note_serialize.data, status=status.HTTP_200_OK)
            
    except Notes.DoesNotExist:
        return HttpResponse("Invalid", status=status.HTTP_400_BAD_REQUEST)
    




