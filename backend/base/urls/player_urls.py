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
    path('samplePlayer/add', views.add_sample_player, name='add_sample_player'),
    path('samplePlayer/update/<int:pk>', views.update_sample_player, name='update_sample_player'),
    path('samplePlayer/remove/<int:pk>', views.remove_sample_player, name='remove_sample_player'),
    path('samplePlayer/<int:pk>', views.get_single_sample_player, name='get_single_sample_player'),
    path('samplePlayer', views.get_all_sample_players, name='all_sample_players'),
] + urlpatterns