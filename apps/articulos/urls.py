# articulos/urls.py
from django.urls import path # type: ignore
from . import views
from .views import (
    ArticuloListView, ArticuloDetailView, ArticuloCreateView, 
    ArticuloUpdateView, ArticuloDeleteView, registro_miembro, agregar_comentario
)

app_name = 'articulos' # El namespace es 'articulos'

urlpatterns = [
    # Funciones de Miembro
    path('registro/', registro_miembro, name='path_registro_miembro'),

    # CRUD de Artículos (CBVs)
    path('', ArticuloListView.as_view(), name='path_listar_articulos'),
    path('crear/', ArticuloCreateView.as_view(), name='path_crear_articulo'),
    path('detalle/<int:pk>/', ArticuloDetailView.as_view(), name='path_detalle_articulo'),
    path('modificar/<int:pk>/', ArticuloUpdateView.as_view(), name='path_modificar_articulo'),
    path('eliminar/<int:pk>/', ArticuloDeleteView.as_view(), name='path_eliminar_articulo'),
    
    # Comentarios
    path('comentar/<int:pk>/', agregar_comentario, name='path_agregar_comentario'),
]