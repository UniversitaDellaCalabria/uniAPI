from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
]

# JWT
urlpatterns += [
    # per ottenere access + refresh token
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # per rinnovare access token usando refresh token  
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),  
]

urlpatterns += [
    # Il file schema vero e proprio
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    # L'interfaccia grafica
    path('docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += [path('', include('agid.urls'))]

for version in settings.REST_FRAMEWORK.get('ALLOWED_VERSIONS', []):
    urlpatterns += [
        path(f'{version}/', include(f'api.{version}.urls')),
    ]

if "uni_esse3api" in settings.INSTALLED_APPS:
    urlpatterns += [path('', include('uni_esse3api.urls'))]

