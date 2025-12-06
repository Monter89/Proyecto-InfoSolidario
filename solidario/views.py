from django.shortcuts import render, redirect 
# 1. Importar el modelo Articulo para poder pedirle datos
from apps.articulos.models import Articulo
from apps.usuarios.forms import FormularioContacto
from django.contrib import messages

def Home(request):
    # 2. Pedimos los últimos 4 artículos (ordenados por fecha descendente)
    # [:4] significa "dame solo los primeros 4"
    ultimos_articulos = Articulo.objects.order_by('-fecha_publicacion')[:4]
    
    # 3. Guardamos en un diccionario de contexto
    contexto = {
        'articulos_destacados': ultimos_articulos
    }
    
    # 4. Se lo enviamos al template
    return render(request, 'home.html', contexto)

def Contacto(request):
    # Si alguien envió datos (POST)
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save() #Aquí se guarda en la Base de Datos
            messages.success(request, "¡Gracias! Tu mensaje fue enviado correctamente.")
            return redirect('path_contacto') # Recarga la página limpia
    
    # Si solo está visitando la página (GET)
    else:
        form = FormularioContacto()

    return render(request, 'contacto.html', {'form': form})