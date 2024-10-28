from rest_framework import serializers
from .models import CategoriaModel

# Este sera un serializador para Categorias
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['nombre']