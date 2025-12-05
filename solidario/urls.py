# solidario/urls.py (Proyecto Principal)

from django.contrib import admin  # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='path_home'),
    path('contacto/', views.Contacto, name='path_contacto'),
    
    # 1. Rutas de Autenticación (Login, Logout, etc.)
    path('cuentas/', include('django.contrib.auth.urls')), 

    # 2. Enlazar la nueva app 'articulos'
    path('articulos/', include('articulos.urls')), 

    # 3. Enlazar la nueva app 'articulos'
    path("usuarios/", include("apps.usuarios.urls")),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)