from django.urls import path, include
from seller import views

urlpatterns =[
    path('reg/', views.regseller, name= 'regseller'),
    path('add/', views.addseller, name= 'addseller'),
    path('view/', views.viewseller, name= 'viewseller'),
    path('details/', views.sellerdetails, name= 'sellerdetails'),

]