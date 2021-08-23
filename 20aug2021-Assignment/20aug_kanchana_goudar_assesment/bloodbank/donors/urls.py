from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.donorregister,name='donorregister'),
    path('search/',views.donorsearch,name='donorsearch'),
    path('adddonors/',views.Adddonors,name='Adddonors'),
    path('viewall/',views.Viewalldonors,name='Viewalldonors'),
    path('view/<bloodgroup>',views.Donordetails,name='Donordetails'),
]