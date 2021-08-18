from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.note_create,name='note_create'),
    path('viewall/',views.note_list,name='note_list'),
    path('viewnote/<ntitle>',views.note_details,name='note_details'),
]