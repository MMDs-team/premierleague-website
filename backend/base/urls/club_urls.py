from django.urls import path
from base.views import club_views as views


urlpatterns = [
    path('add', views.add_club, name='add_club'),
    path('update/<int:pk>', views.update_club, name='update_club'),
    path('remove/<int:pk>', views.remove_club, name='remove_club'),
    path('<int:pk>', views.get_single_club, name='get_single_club'),
    path('', views.get_all_clubs, name='all_clubs'),

]



urlpatterns = [
    path('staff/add', views.add_staff, name='add_staff'),
    path('staff/update/<int:pk>', views.update_staff, name='update_staff'),
    path('staff/remove/<int:pk>', views.remove_staff, name='remove_staff'),
    path('staff/<int:pk>', views.get_single_staff, name='get_single_staff'),
    path('staff', views.get_all_staff, name='all_staff'),

] + urlpatterns