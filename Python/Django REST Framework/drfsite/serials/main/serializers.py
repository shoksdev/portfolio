from rest_framework import serializers
from .models import *


# Сериализатор, основанный на модели Serial, автор присваивается автоматически, поле год не выводится
class SerialSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Serial
        fields = ('title', 'desc', 'country', 'date_start', 'genre', 'author',)
