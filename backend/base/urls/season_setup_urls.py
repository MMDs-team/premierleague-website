from django.urls import path
from base.views import season_setup_views as views

urlpatterns = [
    path('', views.setup_season, name='set_up_season')
]
