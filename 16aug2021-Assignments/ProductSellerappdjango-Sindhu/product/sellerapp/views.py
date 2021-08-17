from django.http.response import JsonResponse
from sellerapp.models import Sellerapp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sellerapp.serializers import SellerappSerializer
from sellerapp.models import Sellerapp
# Create your views here.
@csrf_exempt
def sellerapp_list(request):
    if(request.method=="GET"):
        sellersapp=Sellerapp.objects.all()
        sellerapp_serializer=SellerappSerializer(sellersapp,many=True)
        return JsonResponse(sellerapp_serializer.data,safe=False)

@csrf_exempt
def sellerapp_create(request):
    if(request.method=="POST"):
        getsid=(request.POST.get("sid"))
        getsname=(request.POST.get("sname"))
        getsaddress=request.POST.get("saddress")
        getsphonenum=request.POST.get("sphonenum")
        mydata={"sid":getsid,"sname":getsname,"saddress":getsaddress,"sphonenum":getsphonenum}
        sellerapp_serialize=SellerappSerializer(data=mydata)
        if (sellerapp_serialize.is_valid()):
            sellerapp_serialize.save()
            # return HttpResponse("Sucess")
            return JsonResponse(sellerapp_serialize.data)
        else:
            return HttpResponse("Error in serilization")
    # else:
    #     return HttpResponse("GET METHOD")