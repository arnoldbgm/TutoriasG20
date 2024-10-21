from django.contrib import admin
from .models import CategoriasModel, ProductosModel

# Register your models here.
# Metodo 01: Como registar a nivel del Admin
# admin.site.register(CategoriasModel)
# admin.site.register(ProductosModel)

# Metodo 02: Como registar en el admin
@admin.register(CategoriasModel)
class CategoriasAdmin(admin.ModelAdmin):
   list_display =  ["nombre"]

@admin.register(ProductosModel)
class ProductoAdmin(admin.ModelAdmin):
   list_display = ["titulo", "stock", "contenido"]