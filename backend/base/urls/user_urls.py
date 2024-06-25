from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.register_user, name='user_register'),
    path('profile', views.get_user_profile, name='user_profile'),
    path('profile/update', views.update_user_profile, name='user_update_profile'),
    path('', views.get_all_users, name='all_users'),

]
