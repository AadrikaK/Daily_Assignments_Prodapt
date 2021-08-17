from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.addpro, name='addpro'),
    path('viewall/', views.viewpro, name='viewpro'),
  
]

