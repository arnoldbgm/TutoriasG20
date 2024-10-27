from django.db import models

# Create your models here.

class CategoriaModel(models.Model):
   nombre = models.CharField(max_length=150)

   def __str__(self):
      return self.nombre

class ProductosModel(models.Model):
   nombre = models.CharField(max_length=150)
   descripcion = models.TextField()
   stock = models.IntegerField()
   visibilidad = models.BooleanField(default=True)
   categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE, null=True)

   class Meta:
      db_table = 'productos'
