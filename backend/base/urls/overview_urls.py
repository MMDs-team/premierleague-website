from django.urls import path
from base.views import overviews as views


urlpatterns = [
    path('club', views.get_club, name='get_club'),
    path('player', views.get_player, name='get_player'),
    path('table', views.get_table, name='get_table'),
    path('action', views.get_action, name='get_action'),
    path('fixtures', views.get_fixtures, name='get_fixtures'),
]