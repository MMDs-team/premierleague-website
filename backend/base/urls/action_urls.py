from django.urls import path
from base.views import action_views as views


urlpatterns = [
    path('add', views.add_action, name='add_action'),
    path('update/<int:pk>', views.update_action, name='update_action'),
    path('remove/<int:pk>', views.remove_action, name='remove_action'),
    path('<int:pk>', views.get_single_action, name='get_single_action'),
    path('', views.get_all_acitons, name='all_acitons'),

]