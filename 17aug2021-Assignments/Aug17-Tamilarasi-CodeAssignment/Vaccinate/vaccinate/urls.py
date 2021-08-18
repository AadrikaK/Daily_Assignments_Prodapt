from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.myVaccinatePage,name='myVaccinatePage'),
    path('viewall/',views.myVaccinateList,name='myVaccinateList'),
    path('viewvaccinate/<vno>',views.myVaccinateDetails,name='myVaccinateDetails'),
]