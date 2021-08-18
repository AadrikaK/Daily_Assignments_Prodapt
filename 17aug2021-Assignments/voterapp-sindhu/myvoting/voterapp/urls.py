from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.voterapp_create,name='voterapp_create'),
    path('viewall/',views.voterapp_list,name='voterapp_list'),
    path('viewvote/<vid>',views.voterapp_details,name='voterapp_details'),
]

