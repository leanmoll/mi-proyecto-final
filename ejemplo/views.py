from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Leandro"})

def imc (request, peso, altura):
    imc = 1 
    return render(request, "ejemplo/imc.html", {"imc": imc})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html",
                 {"lista_familiares": lista_familiares})