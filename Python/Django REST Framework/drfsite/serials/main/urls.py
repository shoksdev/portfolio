from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'serials', SerialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('serial/create/', SerialCreateView.as_view(), name='serials'),
    # path('serials/', SerialViewSet.as_view({'post': 'create', 'get': 'list'}), name='serials'),
    # path('serials/<int:pk>', SerialViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='serials'),
]
