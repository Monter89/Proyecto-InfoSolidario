# articulos/forms.py
from django import forms # type: ignore
from .models import Articulo, Comentario, Categoria # Importar nuevos modelos

# 1. Formulario CRUD de Artículos
class FormularioArticulo(forms.ModelForm): # CAMBIO: Usa Articulo
	class Meta:
		model = Articulo
		# Campos relevantes para un blog
		fields = ['titulo', 'contenido', 'categoria', 'ubicacion', 'imagen'] 
		widgets = {
			'contenido': forms.Textarea(attrs={'rows': 5}),
		}

# 2. Formulario de Comentario
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3}),
        }

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']