from . import views
from django.urls import path
urlpatterns = [

    path('',views.viewHomepage,name='viewHomepage'),
    path('contactus/',views.contactUs,name='contactUs'),
]