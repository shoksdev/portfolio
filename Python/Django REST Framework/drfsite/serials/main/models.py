from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Serial(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=20, verbose_name='Страна')
    date_start = models.DateField(verbose_name='Дата выхода')
    year = models.IntegerField(default=0, verbose_name='Год выхода')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title
