"""Entrega2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que almacenan la ubicación de nuestras imagenes 
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.principal, name="principal"),
    path('Artesanias',views.artesanias, name="Artesanias"),
    path('Catalogo', views_registros.registros, name="Catalogo"),
    path('Sesion', views.nuevo, name="Sesion"),
    path('formularioArticulo/',views_registros.formularioArticulo, name="Datos"),
    path('registrarArticulo/',views_registros.registrarArticulo, name="RegistrarArticulo"),
    path('consultarComentarioArticulo/',views_registros.consultarComentarioArticulo, name="Compras"),
    path('eliminarCompra/<int:id>/',views_registros.eliminarArticulo, name='EliminarArticulo'),
    path('editarCompras/<int:id>/',views_registros.consultarComentarioIndividualArticulo, name='Articulo'),
    path('comentarioCompra/<int:id>/',views_registros.editarComentarioArticulo, name="EditarArticulo"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)