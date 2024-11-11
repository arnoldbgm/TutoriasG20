# El view es la parte logica de mi endpoint

# APIView
# Mixins
# Generics

from rest_framework import generics
from .models import CategoriaModel
from .serializer import CategoriaSerializer

# Crearemos la logica para un endpoint
class ListCreateCategorias(generics.ListCreateAPIView):
   #  SELECT * FROM categorias
   queryset = CategoriaModel.objects.all()
   serializer_class = CategoriaSerializer