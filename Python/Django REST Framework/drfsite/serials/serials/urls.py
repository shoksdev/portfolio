from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('api/v1/', include('main.urls')),
    path('admin/', admin.site.urls),
]
