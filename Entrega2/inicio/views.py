from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,"inicio/index.html")

def artesanias(request):
    return render(request, "inicio/artesanias.html")

def catalogo(request):
    return render(request, "inicio/catalogo.html")

def nuevo(request):
    return render(request, "inicio/sesion.html")

