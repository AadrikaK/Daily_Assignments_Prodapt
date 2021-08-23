from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from donors.models import Donor
from donors.serialize import DonorSerialize

def donorregister(request):
    return render(request,'register.html')
def donorsearch(request):
    return render(request,'search.html')
@csrf_exempt
def Adddonors(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerialize(data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("No get method is allowed")

@csrf_exempt
def Viewalldonors(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serialize=DonorSerialize(donor,many=True)
        return JsonResponse(donor_serialize.data,safe=False)

@csrf_exempt
def Donordetails(request,bloodgroup):
    try:
        donor=Donor.objects.get(Blood_group=bloodgroup)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid donor id")
    if(request.method=="GET"):
        donor_serialize=DonorSerialize(donor)
        return JsonResponse(donor_serialize.data,safe=False)
    if(request.method=="DELETE"):
        donor.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        donor_serialize=DonorSerialize(donor,data=mydata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return JsonResponse(donor_serialize.data)
        else:
            return JsonResponse(donor_serialize.error)
        
    



