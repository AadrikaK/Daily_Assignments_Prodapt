from . import views
from django.urls import path
urlpatterns = [
    path('addnotes/',views.addNote,name='addnote'),
    path('viewnotes/',views.viewNote,name='viewallnotes'),
    path('viewnotedetails/<id>',views.viewnotedetails,name='singlenotes'),
]