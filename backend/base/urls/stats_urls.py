from django.urls import path
from base.views import stats_views as views

urlpatterns = [
    path('', views.get_each_actions_best, name='get_each_actions_best'),
    path('top/club', views.stats_top_club, name='stats_top_club'),
    path('top/player', views.stats_top_player, name='stats_top_player'),
    path('top/allTime/clubs', views.stats_top_clubs_all_time, name='stats_top_clubs_all_time'),
    path('top/allTime/players', views.stats_top_players_all_time, name='stats_top_players_all_time'),
]