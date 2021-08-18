from django.shortcuts import render
from voterapp.models import Voterapp
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from voterapp.serializers import VoterappSerializer
from voterapp.models import Voterapp
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
def voterapp_details(request,vid):
    try:
        votersapp=Voterapp.objects.get(vid=vid)
        if(request.method=="GET"):
            voterapp_serializer=VoterappSerializer(votersapp)
            return JsonResponse(voterapp_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            votersapp.delete()
            return HttpResponse("Delete",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            voterapp_serialize=VoterappSerializer(votersapp,data=mydata)
            if(voterapp_serialize.is_valid()):
                voterapp_serialize.save()
                return JsonResponse(voterapp_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(voterapp_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Voterapp.DoesNotExist:
        return HttpResponse("Invalid Voterid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def voterapp_list(request):
    if(request.method=="GET"):
        votersapp=Voterapp.objects.all()
        voterapp_serializer=VoterappSerializer(votersapp,many=True)
        return JsonResponse(voterapp_serializer.data,safe=False)
@csrf_exempt
def voterapp_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        voterapp_serialize=VoterappSerializer(data=mydata)
        if(voterapp_serialize.is_valid()):
            voterapp_serialize.save()
            return JsonResponse(voterapp_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

