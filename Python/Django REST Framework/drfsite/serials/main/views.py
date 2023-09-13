from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .filters import SerialFilter
from .serializers import SerialSerializer
from .models import Serial
from .permissions import MainPermissions
from .pagination import MainPagination


# Вью для создания записи (доступна только аутентифицированным пользователям)
class SerialCreateView(generics.CreateAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [IsAuthenticated, ]


# Вью, отвечающая за всё остальное (редактирование, удаление, вывод списком, вывод отдельной записи)
class SerialViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [MainPermissions, ]  # Кастомные разрешения, подробнее в файле permissions.py
    pagination_class = MainPagination  # Кастомная пагинация, подробнее в файле pagination.py
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = SerialFilter  # Кастомный фильтр, подробнее в файле filters.py
