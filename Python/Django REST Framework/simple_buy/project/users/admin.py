from django.contrib import admin  # Импортируем функционал для работы с админ-панелью

from .models import CustomUser  # Импортируем кастомного пользователя


# Регистрируем пользователя в админ-панели
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
