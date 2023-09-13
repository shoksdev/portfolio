from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('main.urls')),
    path('api/v1/api-auth/', include('rest_framework.urls')),  # Стандартная аутентификация DRF
    path('admin/', admin.site.urls),
]
