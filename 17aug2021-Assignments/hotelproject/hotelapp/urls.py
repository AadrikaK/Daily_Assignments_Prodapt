from django.urls import path,include
from hotelapp import views

urlpatterns=[
    path('add/', views.Hotel, name='Hotel'),
    path('view/', views.hotellist, name='hotellist'),
    path('viewh/', views.myhotel, name='myhotel'),
    
]