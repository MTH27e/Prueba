
from django.contrib import admin
from django.urls import path, include

# Configuración para archivos multimedia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Aplicación de usuarios
    path('', include('app_usuarios.urls')),

    # Aplicación de cartelera
    path('cartelera/', include('app_cartelera.urls')),
]

# Permitir visualizar imágenes durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
