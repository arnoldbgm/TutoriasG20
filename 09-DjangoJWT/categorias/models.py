from django.db import models

class CategoriasModel(models.Model):

   # Creamos la tabla categorias => con el campo nombre
   
   nombre = models.CharField(max_length=255)

   class Meta:
      db_table = "categorias"