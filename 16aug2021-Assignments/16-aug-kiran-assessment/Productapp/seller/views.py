from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerSerializer
from seller.models import Seller
# Create your views here.
@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def selleradd(request):
    if(request.method=='POST'):
        sname=request.POST.get("sname")
        seller_id=request.POST.get("seller_id")
        address=request.POST.get("address")
        mobileno=request.POST.get("mobileno")
        dict={"sname":sname,"seller_id":seller_id,"address":address,"mobileno":mobileno}
        seller_serialize=SellerSerializer(data=dict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")