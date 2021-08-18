from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.notes_create,name='notes_create'),
    path('viewall/',views.notes_list,name='notes_list'),
    path('viewnotes/<fetchid>',views.notes_details,name='notes_details'),
    
]