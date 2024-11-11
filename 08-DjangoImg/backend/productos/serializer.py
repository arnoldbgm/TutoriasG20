# La funcion de un Serializador es
# Deserealizar
# Validar
# Especificar que se va mostrar al cliente
from rest_framework import serializers
from .models import CategoriaModel

# Crearemos el serializador
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
      model = CategoriaModel
      fields = "__all__"