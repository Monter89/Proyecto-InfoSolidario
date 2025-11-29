from django.shortcuts import render  # type: ignore

def Home(request):
    return render(request, 'home.html') 

def Contacto(request):
    return render(request, 'contacto.html') 