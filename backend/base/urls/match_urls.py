from django.urls import path
from base.views import match_views as views


urlpatterns = [
    path('add', views.add_match, name='add_match'),
    path('update/<int:pk>', views.update_match, name='update_match'),
    path('remove/<int:pk>', views.remove_match, name='remove_match'),
    path('<int:pk>', views.get_single_match, name='get_single_match'),
    path('', views.get_all_matches, name='all_matches'),

]