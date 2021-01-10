import json
import requests
from django.http import HttpResponse
from rest_framework_mongoengine import generics
from servidor.filters import EquipoFilter
from servidor.models import Equipo, Partido, Jugador
from servidor.serializers import EquipoSerializer, PartidoSerializer

# Create your views here.

class EquipoList(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    # Filters
    def filter_queryset(self, queryset):
        # El equipo que tenga el jugador con el nombre `jugador`
        jugador = self.request.query_params.get("jugador", None)
        if jugador:
            queryset = queryset.filter(jugadores__nombre=jugador)  # Filtra sobre arrays sin poner __in

        filter_equipo = EquipoFilter(self.request.query_params, queryset=queryset)
        return filter_equipo.qs


class EquipoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class PartidoList(generics.ListCreateAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

    # Filters
    def filter_queryset(self, queryset):
        # Todos los partidos de un equipo como local con nombre `local`
        local = self.request.query_params.get("local", None)
        if local:
            equipos_local = Equipo.objects(nombre=local)

            if equipos_local and equipos_local.count() > 0:
                equipo_local = equipos_local[0]
                queryset = queryset.filter(local=equipo_local.id)
            else:
                queryset = Partido.objects.none()

        # Los partidos en los que el equipo local haya marcado más de `goles_local_min` goles
        goles_local = self.request.query_params.get("goles_local_min", None)
        if goles_local:
            goles_local = int(goles_local)
            queryset = queryset.filter(
                goles_local__gt=goles_local)  # __gt === greater than. __gte === greater than or equal

        return queryset


class PartidoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer


def getDatos(request):
    # Generar la peticion
    url = "https://datosabiertos.malaga.eu/recursos/transporte/EMT/EMTocupestacbici/ocupestacbicifiware.json"
    params = {}
    response = requests.get(url, params=params)
    datos = {}

    if response and response.status_code >= 200 and response.status_code < 300:
        json_response = json.dumps(response.json())
        datos = json.loads(
            json_response)  # No hace falta hacerle el load para devolver sólo los datos, pero sí si quiero cargarlos en una vista o para filtros

        # Filtros
        value = request.GET.get("value")
        if value:
            datos = [dato for dato in datos if
                     dato["status"]["value"][1] == value]  # Filtro
            json_response = json.dumps(datos)  # Vuelvo a pasarlo a dump

    return HttpResponse(json_response,
                        content_type="application/json")  # Devuelvo sólo los datos, sin hacerles el load.
