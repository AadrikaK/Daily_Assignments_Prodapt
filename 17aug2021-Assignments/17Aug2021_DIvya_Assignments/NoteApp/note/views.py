import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from note.serializer import NoteSerializer
from note.models import Notes
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def addpage(request):
    if(request.method=="POST"):
        # gettitle = request.POST.get("title")
        # getdesc = request.POST.get("desc")
        # mydata = {"title":gettitle,"desc":getdesc}
        # result = json.dumps(mydata)
        # return HttpResponse(result)
        mydata = JSONParser().parse(request)
        note_serialize = NoteSerializer(data=mydata)
        if (note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization")

    else:
        return HttpResponse("Bye Bye")
@csrf_exempt
def note_list(request):
    if(request.method == "GET"):
        notes = Notes.objects.all()
        note_serialize = NoteSerializer(notes,many= True)
        return JsonResponse(note_serialize.data,safe= False)

@csrf_exempt
def notepage(request,id):
    try:
        notes = Notes.objects.get(id=id)
    except Notes.DoesNotExist:
        return HttpResponse("Invalid Note ID",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        note_serialize = NoteSerializer(notes)
        return JsonResponse(note_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        notes.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata = JSONParser().parse(request)
        note_serialize = NoteSerializer(notes,data=mydata)
        if(note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)






