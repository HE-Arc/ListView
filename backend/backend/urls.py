from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),  # Enable Login drf interface
    path('api/', include('core.urls')),
    path('api/', include('auth0.urls')),
    path('admin/', admin.site.urls),  # Enable admin view
]