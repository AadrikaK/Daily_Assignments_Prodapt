from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Notes.serializers import NotesSerializer
import json
from Notes.models import Notes
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def notes_list(request):
    if(request.method=="GET"):
        notses=Notes.objects.all()
        notes_serialize=NotesSerializer(notses,many=True)
        return JsonResponse(notes_serialize.data,safe=False)


@csrf_exempt
def notes_details(request,fetchid):
    try:
        notses=Notes.objects.get(id=fetchid)
    except Notes.DoesNotExist:
        return HttpResponse("Invalid Notes Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        notes_serialize=NotesSerializer(notses)
        return JsonResponse(notes_serialize.data,safe=False,status=status.HTTP_200_OK)

    if(request.method=="DELETE"):
        notses.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   
    
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        notes_serialize=NotesSerializer(notses,data=mydata)
        if(notes_serialize.is_valid()):
            notes_serialize.save()
            return JsonResponse(notes_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(notes_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    



@csrf_exempt
def notes_create(request):
    if request.method=="POST":
        getTitle=request.POST.get("title")
        getDescription=request.POST.get("description")
        mydata={"title":getTitle,"description":getDescription}
        notes_serialize=NotesSerializer(data=mydata)
        if(notes_serialize.is_valid()):
            notes_serialize.save()
            return JsonResponse(notes_serialize.data,status=status.HTTP_200_OK)
            
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)

        
