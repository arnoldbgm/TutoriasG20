from rest_framework.serializers import ModelSerializer
from .models import CategoriasModel

class CategoriaSerializer(ModelSerializer):
   class Meta:
      model = CategoriasModel
      fields = '__all__'