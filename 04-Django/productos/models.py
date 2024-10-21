from django.db import models

# Create your models here.
class CategoriasModel(models.Model):
   # El id autoincrementables es por defecto
   #variable (columna) = models.TipoDelDato
   nombre = models.CharField(max_length=255)

   #Nombrar la tabla
   class Meta:
      db_table = "categorias"

   def __str__(self):
      return self.nombre

class ProductosModel(models.Model):
   stock = models.IntegerField()
   titulo = models.CharField(max_length=255)
   contenido = models.TextField(blank=True)
   # categoria_id_id
   #categoria  ->  "_id"
   categoria = models.ForeignKey(CategoriasModel, on_delete=models.CASCADE)

   class Meta:
      db_table = "productos"
   
   def __str__(self):
      return self.titulo