# articulos/apps.py
from django.apps import AppConfig # type: ignore

class ArticulosConfig(AppConfig): # CAMBIO: Nombre de la clase
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articulos' # CAMBIO: Nombre del paquete
    verbose_name = 'Plataforma de Artículos Solidarios'