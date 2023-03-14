from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

import config.settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dogs/', include('dogs.api.urls'), name='dog-app'),
    path('keys/', include('keys.api.urls'), name='key-value-app'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(config.settings.MEDIA_URL, document_root=config.settings.MEDIA_ROOT)
