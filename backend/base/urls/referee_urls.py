from django.urls import path
from base.views import referee_views as views


urlpatterns = [
    path('add', views.add_referee, name='add_referee'),
    path('update/<int:pk>', views.update_referee, name='update_referee'),
    path('remove/<int:pk>', views.remove_referee, name='remove_referee'),
    path('<int:pk>', views.get_single_referee, name='get_single_referee'),
    path('', views.get_all_referees, name='referees'),
]