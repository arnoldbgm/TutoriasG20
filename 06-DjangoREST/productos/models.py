from django.db import models

class CategoriaModel(models.Model):
   nombre = models.CharField(max_length=100)

   class Meta:
      db_table = 'categorias' #el nombre de la tabla

class ProductoModel(models.Model):
   nombre = models.CharField(max_length=100)
   descripcion = models.TextField()
   stock = models.IntegerField()
   visibilidad = models.BooleanField(default=True)
   categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)

   class Meta:
      db_table = 'productos'
