from  django.urls import path, include
from . import views

urlpatterns = [

    path('add/', views.sellers_add, name = 'sellers_add'),
    path('viewall/',views.sellers_list, name ='sellers_list'),
    
]