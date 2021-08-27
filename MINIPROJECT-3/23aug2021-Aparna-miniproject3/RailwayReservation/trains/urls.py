from django.urls import path
from . import views
urlpatterns = [

    # API's
    path('addtrain/',views.trainPage,name="trainPage"),
    path('viewalltrains/',views.trains_list,name="trains_list"),
    path('viewtrain/<id>',views.train_details,name="train_details"),
    path('searchtrain/',views.search_api,name="search_api"),
    path('updatesearchtrain/',views.update_search_api,name="update_search_api"),
    path('deletesearchtrain/',views.delete_search_api,name="update_search_api"),
    path('update_api/',views.update_data_read,name="update_data_read"),
    path('delete_api/',views.delete_data_read,name="delete_data_read"),

    

    # views
    path('home/',views.home_page,name="home_page"),
    path('add/',views.add_train,name="add_train"),
    path('viewall/',views.view_all,name="view_all"),
    path('update/',views.update_train,name="update_train"),
    path('delete/',views.delete_train,name="delete_train"),
    path('search/',views.search_train,name="search_train"),



]