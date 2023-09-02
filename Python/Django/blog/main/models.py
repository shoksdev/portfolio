from django.db import models
from django.contrib.auth.models import AbstractUser


class Article(models.Model): #Данные о статье
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Текст статьи')
    author = models.CharField(max_length=30, verbose_name='Имя автора')
    date_published = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(upload_to='image/%M', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title, self.author}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model): #Комментарий
    email = models.EmailField(verbose_name='Адрес электронной почты')
    nickname = models.CharField(max_length=50, verbose_name='Имя комментатора')
    content = models.TextField(verbose_name='Текст комментарий')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')

    def __str__(self):
        return f'{self.nickname, self.article}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class ArticleLike(models.Model): #Лайк на статью
    ip = models.CharField(max_length=50, verbose_name='IP-адрес')
    art = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')

class CommentLike(models.Model): #Лайк на комментарий
    ip = models.CharField(max_length=50, verbose_name='IP-адрес')
    com = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Комментарий')