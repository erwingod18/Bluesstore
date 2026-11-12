from django.contrib import admin
from .models import Categoria
# Register your models here.

from django.contrib import admin
from .models import Categoria, Instrumento


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'fecha_ingreso', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')