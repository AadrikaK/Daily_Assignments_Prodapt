
from django.urls import path, include
from product import views

urlpatterns = [
    path('detailsreg/', views.regpro , name='regpro'),
    path('addpro/', views.addpro , name='addpro'),
    path('viewpro/', views.viewpro , name='viewpro'),
    path('prodetails/<id>', views.details , name='details'),

]