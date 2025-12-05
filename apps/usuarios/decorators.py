from django.shortcuts import redirect
from django.contrib import messages

def colaborador_required(view_func):
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.error(request, "Debes iniciar sesión.")
            return redirect("login")

        if not hasattr(request.user, "perfil") or not request.user.perfil.es_colaborador:
            messages.error(request, "No tienes permisos para esta acción.")
            return redirect("articulos:path_listar_articulos")

        return view_func(request, *args, **kwargs)

    return wrapper
