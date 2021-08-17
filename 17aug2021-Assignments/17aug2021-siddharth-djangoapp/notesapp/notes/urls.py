from . import views
from django.urls import path,include

urlpatterns = [
    path('addnote/',views.note_add,name='note_add'),
    path('shownotes/',views.all_notes,name='all_notes'),
    path('viewnote/<id>',views.note_info,name='note_info'),
]