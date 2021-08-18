
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('add/', views.vegitable,name='vegitable'),
    path('viewall/',views.vegitable_list,name='vegitable_list'),
    path('viewvegitable/<fetchid>',views.vegitabledetail,name='vegitabledetail')
]
