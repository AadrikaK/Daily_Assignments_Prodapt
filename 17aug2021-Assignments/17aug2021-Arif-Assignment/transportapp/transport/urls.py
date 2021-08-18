from django.urls import path,include
from .import views

urlpatterns = [
    path('add/',views.transport_create, name='transport_create'),
    path('viewall/',views.transport_list,name='transport_list'),
    path('viewdata/<fetchid>',views.transport_details,name='transport_details'),
    
]