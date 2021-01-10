from django.urls import path
from cliente import views

urlpatterns = [
    path('equipos/', views.equipos_vista),
    path('anadir_equipo/', views.anadir_equipo),
    path('ver_datos/', views.verDatos)
]