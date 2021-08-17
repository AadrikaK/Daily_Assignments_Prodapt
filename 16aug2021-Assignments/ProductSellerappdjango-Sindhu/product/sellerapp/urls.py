from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.sellerapp_create,name='sellerapp_create'),
    path('viewall/',views.sellerapp_list,name='sellerapp_list'),
]