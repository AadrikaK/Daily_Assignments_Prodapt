from . import views
from django.urls import path
urlpatterns = [
    path('addpatient/',views.addPat,name='addPat'),
    path('viewpatient/',views.viewPat,name='viewpatient'),
    path('viewpatientdetails/<id>',views.viewpatdetails,name='patientdetails'),
]