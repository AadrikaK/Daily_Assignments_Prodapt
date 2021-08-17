from . import views
from django.urls import path,include

urlpatterns = [
    path('addpersonal/',views.add_Personal,name='add_Personal'),
    path('showpersonals/',views.show_Personals,name='show_Personals'),
    path('viewapersonal/<id>',views.view_a_Personal,name='view_a_Personal'),
]