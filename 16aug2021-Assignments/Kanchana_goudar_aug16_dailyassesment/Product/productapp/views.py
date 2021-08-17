from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductSerializers
from productapp.models import Product

@csrf_exempt
def product_list(request):
    if (request.method=="GET"):
        products=Product.objects.all()
        product_serialize=ProductSerializers(products,many=True)
        return JsonResponse(product_serialize.data,safe=False)


@csrf_exempt
def Myaddpage(request):
    if(request.method=="POST"):
        getcode=request.POST.get("pcode")
        getpname=request.POST.get("pname")
        getdes=request.POST.get("des")
        getprice=request.POST.get("price")
        mydata={"pcode":getcode,"pname":getpname,"des":getdes,"price":getprice}
        product_serialize=ProductSerializers(data=mydata)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("Error in serialization")
        
    else:
        return HttpResponse("No get method is allowed")
