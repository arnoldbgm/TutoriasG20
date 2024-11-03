from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProductosModel, CategoriaModel
from django.contrib.auth.models import User # Es la importacion del modelo de usuarios de Django
from django.contrib.auth.admin import UserAdmin

# @admin.register(ProductosModel)
# # El nombre es al gusto del cliente
# class ProductoAdmin(ModelAdmin):
#    list_display = ["nombre", "stock", "descripcion", "visibilidad", "categoria"]

# @admin.register(CategoriaModel)
# class CategoriaAdmin(ModelAdmin):
#    list_display = ["nombre"]

# Funcion para mostrar el grupo
def get_user_group(user):
   return ", ".join([group.name for group in user.groups.all()])

class CustomUserAdmin(UserAdmin):
   list_display = ['username','first_name', 'email', 'is_staff', 'get_groups']

   # Metodo para mostrar el grupo
   def get_groups(self, obj):
      return get_user_group(obj)
   
   get_groups.short_description = 'Grupos' # Esto cambia el nombre de la columna

# Registrar el modelo en el admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)