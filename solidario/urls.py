# solidario/urls.py (Proyecto Principal)

from django.contrib import admin  # type: ignore
from django.urls import path, include, re_path 
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.views.static import serve
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='path_home'),
    path('contacto/', views.Contacto, name='path_contacto'),
    
    path('cuentas/', include('django.contrib.auth.urls')), 
    path('articulos/', include('apps.articulos.urls')),
    path("usuarios/", include("apps.usuarios.urls")),
] 

# --- CONFIGURACIÓN PARA VER IMÁGENES EN RENDER ---
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)