
from django.db import models


class Pelicula(models.Model):

    # Título de la película
    titulo = models.CharField(max_length=150)

    # Imagen almacenada en la carpeta media/peliculas
    imagen = models.ImageField(upload_to='peliculas/')

    # Representación del nombre de la película
    def __str__(self):
        return self.titulo
