from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.notes_add, name = 'notes_add'),
    path('viewall/',views.notes_list, name ='notes_list'),
    path('viewnotes/<notesid>',views.notes_data,name = 'notes_data'),

]