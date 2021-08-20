from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ProductApp.serializers import ProductSerializer
from ProductApp.models import Product

# Create your views here. 


@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        product1=Product.objects.all()
        product_serializer=ProductSerializer(product1,many=True)
        return JsonResponse(product_serializer.data,safe=False)



@csrf_exempt
def product(request):
    if(request.method=="POST"):
        getname=request.POST.get("pname")
        getcode=request.POST.get("pcode")
        getdescription=request.POST.get("pdescription")
        getprice=request.POST.get("pprice")
        mydict={"pname":getname,"pcode":getcode,"pdescription":getdescription,"pprice":getprice}
        product_serialize=ProductSerializer(data=mydict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)


    else:
        return HttpResponse("error")
