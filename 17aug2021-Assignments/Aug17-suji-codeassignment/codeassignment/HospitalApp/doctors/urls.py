from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.doctorAdd,name='doctorAdd'),
    path('viewall/',views.doctor_list,name='doctor_list'),
    path('viewdoctors/<fetchid>',views.doctor_details,name='doctor_details'),
    
]