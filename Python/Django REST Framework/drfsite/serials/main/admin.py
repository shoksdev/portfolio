from django.contrib import admin
from .models import *

@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'country', 'date_start', 'genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)