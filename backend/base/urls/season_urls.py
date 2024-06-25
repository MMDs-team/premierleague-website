from django.urls import path
from base.views import season_views as views


urlpatterns = [
    path('add', views.add_season, name='add_season'),
    path('update/<int:pk>', views.update_season, name='update_season'),
    path('remove/<int:pk>', views.remove_season, name='remove_season'),
    path('<int:pk>', views.get_single_season, name='get_single_season'),
    path('', views.get_all_seasons, name='all_seasons'),

]