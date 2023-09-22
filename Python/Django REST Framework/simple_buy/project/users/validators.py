# Импортируем необходимый функционал для создания кастомного валидатора
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CustomFIOValidator(validators.RegexValidator):
    regex = r"^[\w]+\s{3}$" # Создаём регулярное выражение, согласно которому username должен представлять собой 3 слова
    message = _(
        "Enter a valid surname, name and patronymic. This value may contain only letters."
    ) # В случае ошибки сообщаем пользователю, что он должен ввести имя, фамилию и отчество, используя только буквы
    flags = 0
