
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.urls import reverse

from .models import Pelicula
from .forms import PeliculaForm


# Verificar si el usuario es administrador
def es_administrador(usuario):

    return (
        usuario.is_authenticated
        and (
            usuario.is_superuser
            or usuario.is_staff
            or usuario.groups.filter(name="Administrador").exists()
        )
    )


# Verificar si el usuario puede consultar la cartelera
def puede_consultar_cartelera(usuario):

    return (
        usuario.is_authenticated
        and (
            usuario.is_superuser
            or usuario.is_staff
            or usuario.groups.filter(
                name__in=["Administrador", "Vendedor", "Cliente"]
            ).exists()
        )
    )


# Guardar películas: solamente el administrador
@never_cache
@login_required
def guardar_pelicula(request):

    if not es_administrador(request.user):
        return HttpResponseForbidden(
            "No tienes permiso para guardar películas."
        )

    if request.method == "POST":

        formulario = PeliculaForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("cartelera:ver_peliculas")

    else:
        formulario = PeliculaForm()

    return render(
        request,
        "cartelera/guardar_pelicula.html",
        {"formulario": formulario}
    )


# Consultar películas: administrador, vendedor y cliente
@never_cache
@login_required
def ver_peliculas(request):

    if not puede_consultar_cartelera(request.user):
        return HttpResponseForbidden(
            "No tienes permiso para consultar la cartelera."
        )

    peliculas = Pelicula.objects.all().order_by("-id")

    # Determinar el panel al que regresará cada usuario
    if request.user.groups.filter(name="Administrador").exists():
        url_volver = reverse("admin_dashboard")

    elif request.user.groups.filter(name="Vendedor").exists():
        url_volver = reverse("vendedor_dashboard")

    else:
        url_volver = reverse("cliente_dashboard")

    return render(
        request,
        "cartelera/ver_peliculas.html",
        {
            "peliculas": peliculas,
            "url_volver": url_volver,
            "puede_guardar": es_administrador(request.user),
        }
    )
    