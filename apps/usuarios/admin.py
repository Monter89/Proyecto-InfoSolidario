from django.contrib import admin
from .models import PerfilUsuario, MensajeContacto

# Esto permite ver quién es colaborador y quién no
admin.site.register(PerfilUsuario)
admin.site.register(MensajeContacto)