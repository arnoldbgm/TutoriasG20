from django.contrib import admin
from .models import CategoriaModel

@admin.register(CategoriaModel)
class CategoriaAdmin(admin.ModelAdmin):
   pass
