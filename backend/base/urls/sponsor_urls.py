from django.urls import path
from base.views import sponsor_views as views


urlpatterns = [
    path('add', views.add_sponsor, name='add_sponsor'),
    path('update/<int:pk>', views.update_sponsor, name='update_sponsor'),
    path('remove/<int:pk>', views.remove_sponsor, name='remove_sponsor'),
    path('<int:pk>', views.get_single_sponsor, name='get_single_sponsor'),
    path('', views.get_all_sponsors, name='all_sponsors'),
]

urlpatterns = [
    path('clubSpon/add', views.add_club_spon, name='add_club_spon'),
    path('clubSpon/remove/<int:pk>', views.remove_club_spon, name='remove_club_spon'),
    path('clubSpon/<int:pk>', views.get_single_club_spon, name='get_single_club_spon'),
    path('clubSpon/', views.get_all_club_spons, name='all_club_spons'),
] + urlpatterns

urlpatterns = [
    path('matchSpon/add', views.add_match_spon, name='add_match_spon'),
    path('matchSpon/update/<int:pk>', views.update_match_spon, name='update_match_spon'),
    path('matchSpon/remove/<int:pk>', views.remove_match_spon, name='remove_match_spon'),
    path('matchSpon/<int:pk>', views.get_single_match_spon, name='get_single_match_spon'),
    path('matchSpon/', views.get_all_match_spons, name='all_match_spons'),
] + urlpatterns

urlpatterns = [
    path('seaSpon/add', views.add_sea_spon, name='add_sea_spon'),
    path('seaSpon/update/<int:pk>', views.update_sea_spon, name='update_sea_spon'),
    path('seaSpon/remove/<int:pk>', views.remove_sea_spon, name='remove_sea_spon'),
    path('seaSpon/<int:pk>', views.get_single_sea_spon, name='get_single_sea_spon'),
    path('seaSpon/', views.get_all_sea_spons, name='all_sea_spons'),
] + urlpatterns