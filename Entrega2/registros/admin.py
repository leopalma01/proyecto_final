from django.contrib import admin
from .models import Catalogos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ( 'nombre', 'material','costo')
    search_fields =( 'nombre', 'material','costo')
    date_hierarchy = 'created'
admin.site.register(Catalogos, AdministrarModelo)