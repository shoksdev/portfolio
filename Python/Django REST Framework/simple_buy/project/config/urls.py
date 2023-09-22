from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('main.urls')),  # Главное API проекта
    path('api-auth/', include('rest_framework.urls')),  # Стандартная аутентификация пользователей DRF
    path('auth/', include('djoser.urls')),  # Аутентификация, регистрация и др. Djoser-а
    path('auth/', include('djoser.urls.authtoken')),  # Аутентификация, регистрация и др. Djoser-а
    path('admin/', admin.site.urls),  # Админ-панель
]
