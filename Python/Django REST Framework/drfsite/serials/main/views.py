from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filters import SerialFilter
from .serializers import SerialSerializer
from .models import Serial, Genre
from .permissions import MainPermissions
from .pagination import MainPagination


class SerialCreateView(generics.CreateAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [IsAuthenticated, ]


class SerialViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [MainPermissions, ]
    authentication_classes = [TokenAuthentication, ]
    pagination_class = MainPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = SerialFilter
