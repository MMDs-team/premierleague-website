from django.urls import path
from base.views import overview_views as views


urlpatterns = [
    path('seasonClubs', views.season_clubs, name='season_clubs'),
    path('allClubs', views.all_clubs, name='all_clubs'),
    path('players', views.get_players, name='get_players'),
    path('tables', views.get_tables, name='get_tables'),    
    # path('actions', views.get_actions, name='get_actions'),
    path('fixtures', views.get_fixtures, name='get_fixtures'),
]