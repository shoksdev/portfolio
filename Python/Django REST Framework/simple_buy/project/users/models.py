# Импортируем функционал, необходимый для создания кастомного юзера
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .validators import CustomFIOValidator  # Импортируем кастомный валидатор


class CustomUser(AbstractUser):
    # Наследуем от AbstractUser-а поля
    username = models.CharField(
        verbose_name='Фамилия Имя Отчество',
        max_length=150,
        help_text=_(
            "Required field. Enter Surname First Name Patronymic"
        ),
        validators=[CustomFIOValidator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )  # username теперь может быть не уникальным, выводится как "Фамилия Имя Отчество" и использует кастомный валидатор
    email = models.EmailField(_("email address"),
                              unique=True)  # email теперь главное поле (логин) и обязан быть уникальным
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"  # В качестве логина теперь используется email
    REQUIRED_FIELDS = ["username"]  # Но ФИО обязан быть при создании суперпользователя
