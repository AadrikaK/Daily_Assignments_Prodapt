from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sellerApp.serializer import sellerSerializer
from sellerApp.models import Seller
# Create your views here.


@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=sellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)


@csrf_exempt
def sellerPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("sname")
        getid=request.POST.get("sid")
        getaddress=request.POST.get("address")
        getPhno=request.POST.get("phno")
        mydata={"sname":getName,"sid":getid,"address":getaddress,"phno":getPhno}
        seller_serialize=sellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(seller_serialize.data)

        else:
            return HttpResponse("Error in serialization")    
        # result=json.dumps(mydict)
        # return HttpResponse(mydata)
    else:
        return HttpResponse("No GET method Allowed")
