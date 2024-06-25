from django.urls import path
from base.views import kit_views as views


urlpatterns = [
    path('add', views.add_kit, name='add_kit'),
    path('update/<int:pk>', views.update_kit, name='update_kit'),
    path('remove/<int:pk>', views.remove_kit, name='remove_kit'),
    path('<int:pk>', views.get_single_kit, name='get_single_kit'),
    path('', views.get_all_kits, name='all_kits'),

]