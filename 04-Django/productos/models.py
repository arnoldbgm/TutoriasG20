from django.db import models

# Create your models here.
class CategoriasModel(models.Model):
   # El id autoincrementables es por defecto
   #variable (columna) = models.TipoDelDato
   nombre = models.CharField(max_length=255)

   #Nombrar la tabla
   class Meta:
      db_table = "categorias"   