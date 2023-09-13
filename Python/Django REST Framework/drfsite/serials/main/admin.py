from django.contrib import admin
from .models import *


# Регистрируем таблицу с сериалами в админ-панель
@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'country', 'date_start', 'genre',)


# Регистрируем таблицу с жанрами в админ-панель
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)
