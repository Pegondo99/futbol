from mongoengine import *


# Create your models here.

class Jugador(EmbeddedDocument):
    nombre = StringField(max_length=50)
    foto = StringField()

class Equipo(Document):
    nombre = StringField(max_length=50)
    puntos = IntField()
    jugadores = ListField(EmbeddedDocumentField(Jugador))


class Partido(Document):
    local = ReferenceField(Equipo, required=True, reverse_delete_rule=CASCADE)
    visitante = ReferenceField(Equipo, required=True, reverse_delete_rule=CASCADE)
    goles_local = IntField()
    goles_visitante = IntField()