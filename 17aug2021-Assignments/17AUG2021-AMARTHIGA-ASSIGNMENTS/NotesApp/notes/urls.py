from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.addnote, name='addnote'),
    path('viewall/', views.viewnote, name='viewnote'),
    path('viewemployee/<id>', views.notes_details, name='notes_details'),
]