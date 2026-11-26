
from django.urls import path
from . import views

urlpatterns = [
    path("", views.iniciar_sesion, name="iniciar_sesion"),

    path("administrador/", views.admin_dashboard, name="admin_dashboard"),

    path("vendedor/", views.vendedor_dashboard, name="vendedor_dashboard"),

    path("cliente/", views.cliente_dashboard, name="cliente_dashboard"),

    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
]

