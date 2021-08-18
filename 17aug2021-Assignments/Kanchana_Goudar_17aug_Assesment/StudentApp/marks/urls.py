from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.Myaddmarks,name='Myaddmarks'),
    path('viewall/',views.Marksview,name='Marksview'),
     path('view/<fetchid>',views.Marks_details,name='Marks_details'),
]