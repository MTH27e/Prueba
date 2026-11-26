
from django.urls import path
from . import views

urlpatterns = [
    # Inicio de sesión
    path("", views.iniciar_sesion, name="iniciar_sesion"),

    # Paneles
    path("administrador/", views.admin_dashboard, name="admin_dashboard"),
    path("vendedor/", views.vendedor_dashboard, name="vendedor_dashboard"),
    path("cliente/", views.cliente_dashboard, name="cliente_dashboard"),

    # Consultas del administrador
    path("usuarios/", views.ver_usuarios, name="ver_usuarios"),
    path("grupos/", views.consultar_grupos, name="consultar_grupos"),
    path("sesiones/", views.consultar_sesion, name="consultar_sesion"),

    # Cerrar sesión
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
]
