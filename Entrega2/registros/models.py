from django.db import models

# Create your models here.
class Catalogos(models.Model): #Define la estructura de nuestra tabla
    nombre = models.TextField(verbose_name="nom") #Texto largo
    material = models.TextField()
    costo = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Catalogo"
        verbose_name_plural = "Catalogos"
        ordering = ["-created"]
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla    

class ComentarioArticulo(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    art = models.TextField(verbose_name="articulo")
    usuario = models.TextField(verbose_name="Nombre")
    email = models.TextField(verbose_name="Correo")
    tel = models.TextField(verbose_name="Telefono")
    dir = models.TextField(verbose_name="Direccion")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Articulo"
        verbose_name_plural = "Comentarios Articulos"
        ordering = ["-created"]
    def __str__(self):
        return self.usuario