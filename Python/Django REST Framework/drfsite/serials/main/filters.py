from django_filters import rest_framework as filters
from .models import Serial


# Фильтр для нахождения сериала по годам
class SerialFilter(filters.FilterSet):
    year = filters.RangeFilter()

    class Meta:
        model = Serial
        fields = ['year']
