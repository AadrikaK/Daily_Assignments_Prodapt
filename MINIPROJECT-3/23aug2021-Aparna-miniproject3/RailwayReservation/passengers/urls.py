from django.urls import path
from . import views
urlpatterns = [
    path('addpassenger/',views.PassengerPage,name="PassengerPage"),
    path('booking/',views.Book_ticket_page,name="Book_ticket_page"),
    path('viewallpassengers/',views.passengers_list,name="passengers_list"),
    path('viewalltickets/',views.tickets_list,name="tickets_list"),
    path('viewpassenger/<id>',views.passenger_details,name="passenger_details"),
    path('searchpassenger/',views.search_api,name="search_api"),
    




    # views
    path('add/',views.add_passenger,name="add_passenger"),
    path('viewall/',views.view_all,name="view_all"),
    path('bookticket/',views.book_ticket,name="book_ticket"),
    path('search/',views.search_passenger,name="search_passenger"),
    # path('update/',views.update_passenger,name="update_passenger"),
    # path('delete/',views.delete_passenger,name="delete_passenger"),
    
]