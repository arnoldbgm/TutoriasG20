from django.db import models

# Create your models here.
class CategoriaModel(models.Model):
   nombre = models.CharField(max_length=100)
   imagen = models.ImageField(upload_to="imagen", null=True)

   # Ponerle nombre a mi tabla
   class Meta:
      db_table = "categorias"