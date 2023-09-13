from django.urls import path, re_path, include
from rest_framework import routers
from .views import *

app_name = 'main'

# Роутер
router = routers.SimpleRouter()
router.register(r'serials', SerialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),  # Аутентификация по почте через djoser
    path('auth/', include('djoser.urls.authtoken')),  # Аутентификация по токену через djoser
    path('serial/create/', SerialCreateView.as_view(), name='serials'),
]
