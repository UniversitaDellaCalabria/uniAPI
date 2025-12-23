from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import api.urls


_prefix = "api"

urlpatterns = [
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
]

# JWT
urlpatterns += [
    # per ottenere access + refresh token
    path(f'{_prefix}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # per rinnovare access token usando refresh token  
    path(f'{_prefix}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]

urlpatterns += [
    path(f'{_prefix}/', include(api.urls)),
]

if "uniEsse3Api" in settings.INSTALLED_APPS:
    import uniEsse3Api.urls
    urlpatterns += [path(f'{_prefix}/', include(uniEsse3Api.urls))]

