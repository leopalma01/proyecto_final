from django.shortcuts import render
from .models import Catalogos
from .forms import ComentarioFormArticulo
from .models import ComentarioArticulo
from django.shortcuts import get_object_or_404
# Create your views here.
def registros(request):
 
    alumnos=Catalogos.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/catalogo.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados
def formularioArticulo(request):
    return render(request,"registros/usuario.html")

def registrarArticulo(request):
    if request.method == 'POST':
        form = ComentarioFormArticulo(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            compras=ComentarioArticulo.objects.all()
            return render(request,"registros/consultaCompras.html",{'compras':compras})
    form = ComentarioFormArticulo()
    return render(request,'registros/usuario.html',{'form': form})

def consultarComentarioArticulo(request):
    compras=ComentarioArticulo.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)
    return render(request,"registros/consultaCompras.html",{'compras':compras})

def eliminarArticulo(request, id,
        confirmacion='registros/eliminarCompra.html'):
        compra = get_object_or_404(ComentarioArticulo, id=id)
        if request.method=='POST':
            compra.delete()
            compras=ComentarioArticulo.objects.all()
            return render(request,"registros/consultaCompras.html",
                {'compras':compras})
        return render(request, confirmacion, {'object':compra})

def consultarComentarioIndividualArticulo(request, id):
        compra=ComentarioArticulo.objects.get(id=id)
        return render(request,"registros/editarCompras.html",
                {'compra':compra})

def editarComentarioArticulo(request, id):
        compra = get_object_or_404(ComentarioArticulo, id=id)
        form = ComentarioFormArticulo(request.POST, instance=compra)

        if form.is_valid():
            form.save() #si el registro ya existe, se modifica.
            compras=ComentarioArticulo.objects.all()
            return render(request,"registros/consultaCompras.html",
                    {'compras':compras})

        return render(request,"registros/editarCompras.html",
                {'compra':compra})
  