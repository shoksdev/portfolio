from rest_framework import pagination


# Пагинация, на странице выводится два объекта из списка, но количество может увеличиваться
class MainPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4
