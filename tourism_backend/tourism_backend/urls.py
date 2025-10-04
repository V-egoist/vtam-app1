# tourism_backend/tourism_backend/urls.py

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # -----------------------------------------------------------
    # API Endpoints
    # -----------------------------------------------------------
    # Direct all requests starting with /api/auth/ to the users app URLs.
    path('api/auth/', include('apps.users.urls')),
    
        path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Maps to /api/auth/token/refresh/
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Other apps will be included here later (e.g., path('api/locations/', ...))
]