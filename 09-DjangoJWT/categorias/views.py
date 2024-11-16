from rest_framework import generics
from .models import CategoriasModel
from .serializer import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated

# Crearemos un endpoint para insertar categorias y traer categorias
# POST - GET
class CreateCategorias(generics.ListCreateAPIView):
   # Cuando estamos usando los generics es necesario
   # queryset  - serializer_class   
   permission_classes = [IsAuthenticated]
   queryset = CategoriasModel.objects.all()
   serializer_class = CategoriaSerializer