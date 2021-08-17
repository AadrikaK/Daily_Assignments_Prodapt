from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.addseller, name='addseller'),
    path('viewall/', views.viewseller, name='viewseller'),
  
]