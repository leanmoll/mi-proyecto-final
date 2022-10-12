from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Leandro"})

def imc (request, peso, altura):
    imc = 1 
    return render(request, "ejemplo/imc.html", {"imc": imc})
