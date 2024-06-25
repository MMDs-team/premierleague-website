from django.urls import path
from base.views import player_views as views


urlpatterns = [
    path('add', views.add_player, name='add_player'),
    path('update/<int:pk>', views.update_player, name='update_player'),
    path('remove/<int:pk>', views.remove_player, name='remove_player'),
    path('<int:pk>', views.get_single_player, name='get_single_player'),
    path('', views.get_all_players, name='all_players'),

]
