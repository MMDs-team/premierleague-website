from django.urls import path
from base.views import action_views as views


urlpatterns = [
    path('add', views.add_action, name='add_action'),
    path('update/<int:pk>', views.update_action, name='update_action'),
    path('remove/<int:pk>', views.remove_action, name='remove_action'),
    path('<int:pk>', views.get_single_action, name='get_single_action'),
    path('', views.get_all_actions, name='all_acitons'),
]

urlpatterns = [
    path('action_type/add', views.add_action_type, name='add_action_type'),
    path('action_type/update/<int:pk>', views.update_action_type, name='update_action_type'),
    path('action_type/remove/<int:pk>', views.remove_action_type, name='remove_action_type'),
    path('action_type/<int:pk>', views.get_single_action_type, name='get_single_action_type'),
    path('action_type', views.get_all_action_types, name='all_acitons_types'),
] + urlpatterns