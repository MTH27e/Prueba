from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cartelera'

urlpatterns = [
    path('cartelera/', include('app_cartelera.urls')),

    path(
        'guardar_pelicula',
        views.guardar_pelicula,
        name='guardar_pelicula'
    ),

    path(
        'ver_peliculas',
        views.ver_peliculas,
        name='ver_peliculas'
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    