from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.addpage,name='addpage'),
    path('viewall/',views.note_list,name='note_list'),
    path('shownote/<id>',views.notepage,name='notepage'),
]