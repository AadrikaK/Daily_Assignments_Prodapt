from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.myNotePage,name='myNotePage'),
    path('viewall/',views.myNoteList,name='myNoteList'),
    path('viewnote/<title>',views.myNoteDetails,name='myNoteDetails'),
]