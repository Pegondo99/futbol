from rest_framework_mongoengine import serializers

from servidor.models import Equipo, Partido


class EquipoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class PartidoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Partido
        fields = '__all__'