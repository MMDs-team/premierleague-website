from django.urls import path
from base.views import employee_views as views


urlpatterns = [
    path('add', views.add_employee, name='add_employee'),
    path('update/<int:pk>', views.update_employee, name='update_employee'),
    path('remove/<int:pk>', views.remove_employee, name='remove_employee'),
    path('<int:pk>', views.get_single_employee, name='get_single_employee'),
    path('', views.get_all_employees, name='all_employees'),
]