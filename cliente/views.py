import cloudinary
from django.shortcuts import render, redirect

# Create your views here.
from servidor.services.services import generate_request, response_2_dict, generate_post


def equipos_vista(request):
    url = "http://127.0.0.1:8000/equipos/"
    response = generate_request(url, {})
    equipos = response_2_dict(response)

    return render(request, "equipos.html", {"equipos": equipos})


def anadir_equipo(request):
    url = "http://127.0.0.1:8000/equipos/"

    jugadores = []
    for i in range(1, int(request.POST["num_jugadores"]) + 1):
        nombre = "nombre_jugador_" + str(i)
        foto = "foto_" + str(i)
        foto_url = ""
        if len(request.FILES) > 0:
            file = request.FILES[foto]
            result = cloudinary.uploader.upload(file, transformation=[
                {'width': 350, 'height': 350, 'crop': 'thumb', }])
            foto_url = result["url"]
        jugadores.append({"nombre": request.POST[nombre], "foto": foto_url})
    print(jugadores)
    generate_post(url, {"nombre": request.POST["nombre"], "puntos": request.POST["puntos"],
                        "jugadores": jugadores})
    print(request.POST)
    return redirect("/cliente/equipos")


def verDatos(request):
    url = "http://127.0.0.1:8000/datos/"
    response = generate_request(url, {})
    datos = response_2_dict(response)

    return render(request, "datos.html", {"datos": datos})
