from django.urls import path
from base.views import player_views as views


urlpatterns = [
    path('add', views.add_player, name='add_player'),
    path('update/<int:pk>', views.update_player, name='update_player'),
    path('remove/<int:pk>', views.remove_player, name='remove_player'),
    path('<int:pk>', views.get_single_player, name='get_single_player'),
    path('', views.get_all_players, name='all_players'),

]


urlpatterns = [
    path('samplePlayer/add', views.add_sample_club, name='add_sample_club'),
    path('samplePlayer/update/<int:pk>', views.update_sample_club, name='update_sample_club'),
    path('samplePlayer/remove/<int:pk>', views.remove_sample_club, name='remove_sample_club'),
    path('samplePlayer/<int:pk>', views.get_single_sample_club, name='get_single_sample_club'),
    path('samplePlayer', views.get_all_sample_clubs, name='all_sample_clubs'),

] + urlpatterns