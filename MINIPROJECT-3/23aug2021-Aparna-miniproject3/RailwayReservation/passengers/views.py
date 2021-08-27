from django.shortcuts import render
from passengers.models import Passenger, Ticket
from passengers.serializers import PassengerSerializer, TicketSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.

def add_passenger(request):
    return render(request,'registerpassenger.html')

def book_ticket(request):
    return render(request,'bookticket.html')


def search_passenger(request):
    return render(request,'searchpassenger.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/passengers/viewallpassengers/").json()

    return render(request,'viewallpassengers.html',{"data":fetchdata})


# def update_passenger(request):
#     return render(request,'updatepassenger.html')

# def delete_passenger(request):
    # return render(request,'deletepassenger.html')

@csrf_exempt
def PassengerPage(request):
    if(request.method=="POST"):
        # passengersdict=JSONParser().parse(request)
        passenger_serializer=PassengerSerializer(data=request.POST)
        if(passenger_serializer.is_valid()):
            passenger_serializer.save()
            return JsonResponse(passenger_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def passengers_list(request):
    if(request.method=="GET"):
        passenger=Passenger.objects.all()
        passenger_serializer=PassengerSerializer(passenger,many=True)
        return JsonResponse(passenger_serializer.data,safe=False)

    

@csrf_exempt
def Book_ticket_page(request):
    if(request.method=="POST"):
        # ticketssdict=JSONParser().parse(request)
        ticket_serializer=TicketSerializer(data=request.POST)
        if(ticket_serializer.is_valid()):
            ticket_serializer.save()
            return JsonResponse(ticket_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def tickets_list(request):
    if(request.method=="GET"):
        ticket=Ticket.objects.all()
        ticket_serializer=TicketSerializer(ticket,many=True)
        return JsonResponse(ticket_serializer.data,safe=False)


@csrf_exempt
def passenger_details(request,id):
    try:
        passengers=Passenger.objects.get(id=id)
        if(request.method =="GET"):
            passengers_serializer=PassengerSerializer(passengers)
            return JsonResponse(passengers_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            passengers.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            passengersdict=JSONParser().parse(request)
            passengers_serializer=PassengerSerializer(passengers,data=passengersdict)
            if(passengers_serializer.is_valid()):
                passengers_serializer.save()
                return JsonResponse(passengers_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(passengers_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Passenger.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_api(request):
    try:
        getUsername = request.POST.get("username")
        getPassenger = Passenger.objects.filter(username=getUsername)
        passenger_serializer = PassengerSerializer(getPassenger, many=True)
        return render(request,"searchpassenger.html",{"data":passenger_serializer.data})
        # return JsonResponse(passenger_serializer.data,safe=False, status=status.HTTP_200_OK)
    except Passenger.DoesNotExist:
        return HttpResponse("Invalid Username",status=status.HTTP_404_NOT_FOUND)








