from . import views
from django.urls import path
urlpatterns = [
    path('adddoctor/',views.addDoc,name='addDoc'),
    path('viewdoctor/',views.viewDoc,name='viewallDoc'),
    path('viewdoctordetails/<id>',views.viewDocdetails,name='docdetails'),
]