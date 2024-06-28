from django.urls import path
from base.views import ticket_views as views




urlpatterns = [
    path('buy', views.buy_ticket, name='buy_ticket'),
    path('remove/<int:pk>', views.cancel_ticket, name='cancel_ticket'),
    path('whatch', views.get_user_ticket, name='get_user_ticket'),  #api/ticket/whatch?us=4
    path('<int:pk>', views.get_single_ticket, name='get_single_ticket'),
    path('', views.get_all_tickets, name='get_all_tickets'),
]


urlpatterns = [
    path('type/add', views.add_ticket_type, name='add_ticket_type'),
    path('type/update/<int:pk>', views.update_ticket_type, name='update_ticket_type'),
    path('type/remove/<int:pk>', views.remove_ticket_type, name='remove_ticket_type'),
    path('type/<int:pk>', views.get_single_ticket_type, name='get_single_ticket_type'),
    path('type', views.get_all_ticket_type, name='all_ticket_types'),
] + urlpatterns