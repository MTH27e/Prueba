from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Pelicula
from .forms import PeliculaForm


def es_administrador(usuario):

    return (
        usuario.is_authenticated
        and (
            usuario.is_superuser
            or usuario.is_staff
            or usuario.groups.filter(name='Administrador').exists()
        )
    )


def guardar_pelicula(request):

    if not es_administrador(request.user):
        return HttpResponseForbidden(
            'No tienes permiso para guardar películas.'
        )

    if request.method == 'POST':

        formulario = PeliculaForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():

            formulario.save()

            return redirect('cartelera:ver_peliculas')

    else:

        formulario = PeliculaForm()

    return render(
        request,
        'cartelera/guardar_pelicula.html',
        {'formulario': formulario}
    )


def ver_peliculas(request):

    peliculas = Pelicula.objects.all().order_by('-id')

    return render(
        request,
        'cartelera/ver_peliculas.html',
        {'peliculas': peliculas}
    )