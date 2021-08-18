from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.addCourier, name = 'addCourier'),
    path('listall/',views.listCourier, name ='listCourier'),
    path('view/<cid>',views.courierData,name = 'courierData'),

]