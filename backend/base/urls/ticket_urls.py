from django.urls import path
from base.views import ticket_views as views




urlpatterns = [
    path('add', views.buy_ticket, name='add_type_stadium'),
    path('remove', views.cancel_ticket, name='add_type_stadium'),
    path('get<int:pk>', views.get_single_ticket, name='get_all_tickets'),
    path('', views.get_all_ticket, name='get_all_tickets'),
]


urlpatterns = [
    path('type/add', views.add_type_stadium, name='add_type_stadium'),
    path('type/update/<int:pk>', views.update_type_stadium, name='update_type_stadium'),
    path('type/remove/<int:pk>', views.remove_type_stadium, name='remove_type_stadium'),
    path('type/<int:pk>', views.get_single_type_stadium, name='get_single_type_stadium'),
    path('type', views.get_all_type_stadium, name='all_type_stadiums'),
] + urlpatterns