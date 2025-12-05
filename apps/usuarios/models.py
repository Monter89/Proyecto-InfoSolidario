from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    es_colaborador = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username