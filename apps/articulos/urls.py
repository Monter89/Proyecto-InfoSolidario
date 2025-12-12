# articulos/urls.py
from django.urls import path # type: ignore
from . import views
from .views import (
    ArticuloListView, ArticuloDetailView, ArticuloCreateView, 
    ArticuloUpdateView, ArticuloDeleteView, agregar_comentario, CategoriaCreateView
)

app_name = 'articulos' # El namespace es 'articulos'

urlpatterns = [
    
    # CRUD de Artículos (CBVs)
    path('', ArticuloListView.as_view(), name='path_listar_articulos'),
    path('crear/', ArticuloCreateView.as_view(), name='path_crear_articulo'),
    path('detalle/<int:pk>/', ArticuloDetailView.as_view(), name='path_detalle_articulo'),
    path('modificar/<int:pk>/', ArticuloUpdateView.as_view(), name='path_modificar_articulo'),
    path('eliminar/<int:pk>/', ArticuloDeleteView.as_view(), name='path_eliminar_articulo'),
    
    # Comentarios
    path('comentar/<int:pk>/', agregar_comentario, name='path_agregar_comentario'),
    # Rutas para Comentarios
    path('comentario/editar/<int:pk>/', views.ComentarioUpdateView.as_view(), name='path_editar_comentario'),
    path('comentario/eliminar/<int:pk>/', views.ComentarioDeleteView.as_view(), name='path_eliminar_comentario'),
    # Rutas para Categorías
    path('categoria/nueva/', CategoriaCreateView.as_view(), name='path_crear_categoria'),
]