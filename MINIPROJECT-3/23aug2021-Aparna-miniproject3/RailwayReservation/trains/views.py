import trains
from django.shortcuts import render
from trains.models import Trains
from trains.serializers import TrainSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json
from django.shortcuts import redirect

# Create your views here.

# -----Views----------

def home_page(request):
    return render(request,'home.html')

def add_train(request):
    return render(request,'addtrain.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/trains/viewalltrains/").json()

    return render(request,'viewtrains.html',{"data":fetchdata})

def update_train(request):
    return render(request,'updatetrain.html')

def delete_train(request):
    return render(request,'deletetrain.html')

def search_train(request):
    return render(request,'search.html')


# ----API's-------
@csrf_exempt
def trainPage(request):
    if(request.method=="POST"):
        # trainsdict=JSONParser().parse(request)
        train_serializer=TrainSerializer(data=request.POST)
        if(train_serializer.is_valid()):
            train_serializer.save()
            return JsonResponse(train_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def trains_list(request):
    if(request.method=="GET"):
        train=Trains.objects.all()
        train_serializer=TrainSerializer(train,many=True)
        return JsonResponse(train_serializer.data,safe=False)


@csrf_exempt
def train_details(request,id):
    try:
        trains=Trains.objects.get(id=id)
        if(request.method =="GET"):
            trains_serializer=TrainSerializer(trains)
            return JsonResponse(trains_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            trains.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            trainsdict=JSONParser().parse(request)
            trains_serializer=TrainSerializer(trains,data=trainsdict)
            if(trains_serializer.is_valid()):
                trains_serializer.save()
                return JsonResponse(trains_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(trains_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Trains.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_api(request):
    try:
        getTrainNumber = request.POST.get("trainNumber")
        getTrain = Trains.objects.filter(trainNumber=getTrainNumber)
        train_serializer = TrainSerializer(getTrain, many=True)
        return render(request,"search.html",{"data":train_serializer.data})
        # return JsonResponse(train_serializer.data,safe=False, status=status.HTTP_200_OK)
    except Trains.DoesNotExist:
        return HttpResponse("Invalid From Station",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Error")

@csrf_exempt
def update_search_api(request):
    try:
        getTrainNumber = request.POST.get("trainNumber")
        getTrain = Trains.objects.filter(trainNumber=getTrainNumber)
        train_serializer = TrainSerializer(getTrain, many=True)

        return render(request,"updatetrain.html",{"data":train_serializer.data})
        # return JsonResponse(train_serializer.data,safe=False, status=status.HTTP_200_OK)
    except:
        return HttpResponse("Invalid From Station",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def update_data_read(request):
    getId = request.POST.get("newid")

    getTrainname = request.POST.get("newtrain_name")
    getTrainnumber = request.POST.get("newtrain_no")
    getFromstation = request.POST.get("newfrom_station")
    getTostation = request.POST.get("newto_station")
    getRunnindays = request.POST.get("newrunning_days")
    

    mydata={'trainName':getTrainname,'trainNumber':getTrainnumber,'fromStation':getFromstation,'toStation':getTostation,'runningDays':getRunnindays}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/trains/viewtrain/" + getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Data updated successfully")


@csrf_exempt
def delete_search_api(request):
    try:
        getTrainNumber = request.POST.get("trainNumber")
        getTrain = Trains.objects.filter(trainNumber=getTrainNumber)
        train_serializer = TrainSerializer(getTrain, many=True)
        return render(request,"deletetrain.html",{"data":train_serializer.data})
    except:
        return HttpResponse("Invalid From Station")



@csrf_exempt
def delete_data_read(request):

    getId = request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/trains/viewtrain/" + getId
    requests.delete(ApiLink)
    return HttpResponse("Data deleted successfully")

    