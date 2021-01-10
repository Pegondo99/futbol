import django_mongoengine_filter

from servidor.models import Equipo


class EquipoFilter(django_mongoengine_filter.FilterSet):
    nombre = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')
    puntos = django_mongoengine_filter.filters.StringFilter(lookup_type='contains')

    class Meta:
        model = Equipo
        fields = []