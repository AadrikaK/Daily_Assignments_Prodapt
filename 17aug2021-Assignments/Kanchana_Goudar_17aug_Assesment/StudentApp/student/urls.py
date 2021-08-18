from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.MyaddStudent,name='MyaddStudent'),
    path('viewall/',views.Studentview,name='Studentview'),
    path('view/<fetchid>',views.Student_details,name='Student_details'),
]