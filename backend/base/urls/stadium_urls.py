from django.urls import path
from base.views import stadium_views as views


urlpatterns = [
    path('add', views.add_stadium, name='add_stadium'),
    path('update/<int:pk>', views.update_stadium, name='update_stadium'),
    path('remove/<int:pk>', views.remove_stadium, name='remove_stadium'),
    path('<int:pk>', views.get_single_stadium, name='get_single_stadium'),
    path('', views.get_all_stadiums, name='all_stadiums'),

]


urlpatterns = [
    path('clubStad/add', views.add_club_stadium, name='add_club_stadium'),
    path('clubStad/remove/<int:pk>', views.remove_club_stadium, name='remove_club_stadium'),
    path('clubStad/<int:pk>', views.get_single_club_stadium, name='get_single_club_stadium'),
    path('clubStad', views.get_all_club_stadium, name='all_club_stadium'),

] + urlpatterns