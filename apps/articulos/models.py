# articulos/models.py
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.utils import timezone # type: ignore

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = "Categorías"
    def __str__(self):
        return self.nombre

class Articulo(models.Model): 
    titulo = models.CharField(max_length=200) 
    contenido = models.TextField() 
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    # --- LISTA REDUCIDA (SOLO NEA) ---
    PROVINCIAS_CHOICES = [
        ('Chaco', 'Chaco'),
        ('Corrientes', 'Corrientes'),
        ('Formosa', 'Formosa'),
        ('Misiones', 'Misiones'),
    ]
    ubicacion = models.CharField(
        max_length=50, 
        choices=PROVINCIAS_CHOICES, 
        default='Chaco', 
        verbose_name='Provincia'
    )
    imagen = models.ImageField(upload_to='articulos/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='articulos')
    class Meta:
        ordering = ['-fecha_publicacion']
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['fecha_creacion']
    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.articulo.titulo}'