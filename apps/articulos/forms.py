# articulos/forms.py
from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Articulo, Comentario # Importar nuevos modelos

# 1. Formulario de Registro (Miembro)
class FormularioRegistroMiembro(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "first_name", "last_name")

# 2. Formulario CRUD de Artículos
class FormularioArticulo(forms.ModelForm): # CAMBIO: Usa Articulo
	class Meta:
		model = Articulo
		# Campos relevantes para un blog
		fields = ['titulo', 'contenido', 'categoria', 'imagen'] 
		widgets = {
			'contenido': forms.Textarea(attrs={'rows': 5}),
		}

# 3. Formulario de Comentario
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3}),
        }