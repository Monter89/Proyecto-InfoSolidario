from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import FormularioRegistroMiembro

def registro(request):
    if request.method == "POST":
        form = FormularioRegistroMiembro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro completado con éxito.")
            return redirect("articulos:path_listar_articulos")
    else:
        form = FormularioRegistroMiembro()

    return render(request, "usuarios/registro.html", {"form": form})
