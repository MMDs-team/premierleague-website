from django.urls import path
from base.views import stadium_views as views


urlpatterns = [
    path('add', views.add_stadium, name='add_stadium'),
    path('update/<int:pk>', views.update_stadium, name='update_stadium'),
    path('remove/<int:pk>', views.remove_stadium, name='remove_stadium'),
    path('<int:pk>', views.get_single_stadium, name='get_single_stadium'),
    path('', views.get_all_stadiums, name='all_stadiums'),

]