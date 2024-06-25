from django.urls import path
from base.views import sponsor_views as views


urlpatterns = [
    path('add', views.add_sponsor, name='add_sponsor'),
    path('update/<int:pk>', views.update_sponsor, name='update_sponsor'),
    path('remove/<int:pk>', views.remove_sponsor, name='remove_sponsor'),
    path('<int:pk>', views.get_single_sponsor, name='get_single_sponsor'),
    path('', views.get_all_sponsors, name='all_sponsors'),

]