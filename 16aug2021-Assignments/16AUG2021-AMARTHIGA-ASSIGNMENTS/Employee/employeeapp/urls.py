from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.addemp, name='addemp'),
    path('viewall/', views.viewemp, name='viewemp'),
]