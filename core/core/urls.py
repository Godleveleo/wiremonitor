from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('core/backend/', admin.site.urls),
    path('', include('monitor.urls')),
    path('auth/', include('authAccount.urls')),
    
    

]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )