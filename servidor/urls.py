from django.urls import path
from servidor import views

urlpatterns = [
    path('equipos/', views.EquipoList.as_view()),
    path('equipos/<str:id>', views.EquipoDetails.as_view()),
    path('partidos/', views.PartidoList.as_view()),
    path('partidos/<str:id>', views.PartidoDetails.as_view()),
    path('datos/', views.getDatos),
]
