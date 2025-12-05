# articulos/views.py
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.urls import reverse_lazy, reverse # type: ignore
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.contrib import messages # type: ignore
from django.db.models import Q  # type: ignore

# Asegúrate de que estos archivos existan en la carpeta 'articulos'
from .models import Articulo, Categoria, Comentario 
from .forms import FormularioArticulo, FormularioComentario


# --- Mixin de Seguridad Personalizado (Requisito de Perfiles) ---
class AutorOAdminMixin(UserPassesTestMixin, LoginRequiredMixin):
    # Condición: Solo el autor del artículo o el Admin (is_staff) puede realizar la acción
    def test_func(self):
        obj = self.get_object() 
        return obj.autor == self.request.user or self.request.user.is_staff
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para realizar esta acción.")
        return redirect('articulos:path_listar_articulos')


# ---------------------------------------------
# 1. LISTAR ARTÍCULOS (ListView)
# ---------------------------------------------
class ArticuloListView(ListView):
    model = Articulo 
    context_object_name = 'articulos' 
    template_name = 'articulos/listar.html' 
    
    # Implementación de Filtros y Ordenamiento (Requisito de la consigna)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all() # Para el menú de filtros
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        orden = self.request.GET.get('orden')
        if orden == 'antiguedad_asc': 
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'alfabetico_asc':
            queryset = queryset.order_by('titulo')
        elif orden == 'alfabetico_desc':
            queryset = queryset.order_by('-titulo')
        
        return queryset


# ---------------------------------------------
# 2. CREAR ARTÍCULO (CreateView) - SOLO MIEMBROS
# ---------------------------------------------
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login') 
    model = Articulo
    form_class = FormularioArticulo
    template_name = 'articulos/crear.html' 
    success_url = reverse_lazy('articulos:path_listar_articulos') 

    def form_valid(self, form):
        form.instance.autor = self.request.user 
        return super().form_valid(form)


# ---------------------------------------------
# 3. DETALLE DE ARTÍCULO (DetailView)
# ---------------------------------------------
class ArticuloDetailView(DetailView):
    model = Articulo
    context_object_name = 'articulo' 
    template_name = 'articulos/detalle.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comentario'] = FormularioComentario() 
        return context


# ---------------------------------------------
# 4. MODIFICAR/ELIMINAR ARTÍCULO - SOLO AUTOR/ADMIN
# ---------------------------------------------
class ArticuloUpdateView(AutorOAdminMixin, UpdateView):
    model = Articulo
    form_class = FormularioArticulo
    template_name = 'articulos/modificar.html'
    
    def get_success_url(self):
        messages.success(self.request, "Artículo modificado con éxito.")
        return reverse('articulos:path_detalle_articulo', kwargs={'pk': self.object.pk})

class ArticuloDeleteView(AutorOAdminMixin, DeleteView):
    model = Articulo
    template_name = 'articulos/eliminar.html'
    success_url = reverse_lazy('articulos:path_listar_articulos')

# ---------------------------------------------
# 5. AGREGAR COMENTARIO (Función - Requiere Login)
# ---------------------------------------------
@login_required(login_url=reverse_lazy('login'))
def agregar_comentario(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    
    if request.method == 'POST':
        form = FormularioComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user 
            comentario.save()
            messages.success(request, "Comentario publicado correctamente.")
    
    return redirect('articulos:path_detalle_articulo', pk=pk)