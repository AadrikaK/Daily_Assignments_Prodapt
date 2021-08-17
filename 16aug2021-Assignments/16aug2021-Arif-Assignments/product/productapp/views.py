from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductSerializer
from productapp.models import Product

@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        k=Product.objects.all()
        product_serializer=ProductSerializer(k,many=True)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def product_create(request):
    if (request.method=="POST"):
        getName=request.POST.get("name")
        getProductCode=request.POST.get("pcode")
        getProductDescription=request.POST.get("pdes")
        getProductPrice=request.POST.get("pprice")
        mydata={"name":getName,"pcode":getProductCode,"pdes":getProductDescription,"pprice":getProductPrice}
        product_serialize=ProductSerializer(data=mydata)
        #result=json.dumps(mydict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("no get")

