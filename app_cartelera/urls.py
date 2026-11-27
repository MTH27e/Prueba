
from django.urls import path
from . import views

app_name = "cartelera"

urlpatterns = [

    # Consultar películas
    path(
        "peliculas/",
        views.ver_peliculas,
        name="ver_peliculas"
    ),

    # Registrar películas
    path(
        "guardar/",
        views.guardar_pelicula,
        name="guardar_pelicula"
    ),

]
