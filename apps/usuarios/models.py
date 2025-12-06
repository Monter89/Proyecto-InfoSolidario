from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    es_colaborador = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True) # Se guarda la fecha sola

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.email}"