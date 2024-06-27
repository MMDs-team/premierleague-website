from django.urls import path
from base.views import stats_views as views


urlpatterns = [
    path('top/club', views.stats_top_club, name='add_stadium'),
    path('top/player', views.status_top_player, name='add_stadium'),
]