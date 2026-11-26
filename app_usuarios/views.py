
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.sessions.models import Session
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


# Redirigir según el grupo del usuario
def redireccionar_grupo(user):

    if user.groups.filter(name="Administrador").exists():
        return redirect("admin_dashboard")

    elif user.groups.filter(name="Vendedor").exists():
        return redirect("vendedor_dashboard")

    elif user.groups.filter(name="Cliente").exists():
        return redirect("cliente_dashboard")

    return None


# Inicio de sesión
@never_cache
def iniciar_sesion(request):

    if request.user.is_authenticated:
        respuesta = redireccionar_grupo(request.user)

        if respuesta:
            return respuesta

        logout(request)

    if request.method == "POST":

        usuario = request.POST.get("username")
        contrasena = request.POST.get("password")

        user = authenticate(
            request,
            username=usuario,
            password=contrasena
        )

        if user is not None:

            login(request, user)

            respuesta = redireccionar_grupo(user)

            if respuesta:
                return respuesta

            logout(request)

            return render(request, "usuarios/login.html", {
                "error": "El usuario no tiene un grupo asignado."
            })

        return render(request, "usuarios/login.html", {
            "error": "Usuario o contraseña incorrectos."
        })

    return render(request, "usuarios/login.html")


# Panel del administrador
@never_cache
@login_required
def admin_dashboard(request):

    if not request.user.groups.filter(name="Administrador").exists():
        raise PermissionDenied

    return render(request, "usuarios/admin_dashboard.html")


# Consultar usuarios
@never_cache
@login_required
def ver_usuarios(request):

    if not request.user.groups.filter(name="Administrador").exists():
        raise PermissionDenied

    usuarios = User.objects.all().prefetch_related("groups")

    return render(request, "usuarios/ver_usuarios.html", {
        "usuarios": usuarios
    })


# Consultar grupos
@never_cache
@login_required
def consultar_grupos(request):

    if not request.user.groups.filter(name="Administrador").exists():
        raise PermissionDenied

    grupos = Group.objects.all().prefetch_related("user_set")

    return render(request, "usuarios/consultar_grupos.html", {
        "grupos": grupos
    })


# Consultar sesiones
@never_cache
@login_required
def consultar_sesion(request):

    if not request.user.groups.filter(name="Administrador").exists():
        raise PermissionDenied

    sesiones = Session.objects.filter(
        expire_date__gte=timezone.now()
    )

    return render(request, "usuarios/consultar_sesion.html", {
        "sesiones": sesiones
    })


# Panel del vendedor
@never_cache
@login_required
def vendedor_dashboard(request):

    if not request.user.groups.filter(name="Vendedor").exists():
        raise PermissionDenied

    return render(request, "usuarios/vendedor_dashboard.html")


# Panel del cliente
@never_cache
@login_required
def cliente_dashboard(request):

    if not request.user.groups.filter(name="Cliente").exists():
        raise PermissionDenied

    return render(request, "usuarios/cliente_dashboard.html")


# Cerrar sesión
@never_cache
@require_POST
@login_required
def cerrar_sesion(request):

    logout(request)

    return redirect("autenticacion")
