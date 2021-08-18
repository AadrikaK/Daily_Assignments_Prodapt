from django.urls import path,include
from notes import views
urlpatterns=[
    path('add/',views.notes_create,name='notes_create'),
    path('viewall/',views.notes_list,name='notes_list'),
    path('viewnotes/<id>',views.notes_details,name='notes_details'),
    
]