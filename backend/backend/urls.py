from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('base.urls.user_urls')),
    path('api/season/', include('base.urls.season_urls')),
    path('api/club/', include('base.urls.club_urls')),
    path('api/player/', include('base.urls.player_urls')),
    path('api/match/', include('base.urls.match_urls')),
    path('api/action/', include('base.urls.action_urls')),
    path('api/referee/', include('base.urls.referee_urls')),
    path('api/employee/', include('base.urls.employee_urls')),
    path('api/stadium/', include('base.urls.referee_urls')),
    path('api/kit/', include('base.urls.kit_urls')),
    path('api/sponsor/', include('base.urls.sponsor_urls')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)