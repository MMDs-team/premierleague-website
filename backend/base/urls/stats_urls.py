from django.urls import path
from base.views import stats_views as views


urlpatterns = [
    path('top/club', views.stats_top_club, name='stats_top_club'),
    path('top/player', views.status_top_player, name='status_top_player'),
    path('top/allTime/club', views.stats_top_club_all_time, name='stats_top_club_all_time'),
    path('top/allTime/player', views.status_top_player_all_time, name='status_top_player_all_time'),
]