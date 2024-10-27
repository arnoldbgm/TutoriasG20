from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProductosModel, CategoriaModel

@admin.register(ProductosModel)
# El nombre es al gusto del cliente
class ProductoAdmin(ModelAdmin):
   list_display = ["nombre", "stock", "descripcion", "visibilidad", "categoria"]

@admin.register(CategoriaModel)
class CategoriaAdmin(ModelAdmin):
   list_display = ["nombre"]