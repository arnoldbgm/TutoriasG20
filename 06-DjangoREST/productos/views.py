from rest_framework import generics
from .models import CategoriaModel
from .serializers import CategoriasSerializer

# Endpoint para mostrar todas las categorias
class ListCategorias(generics.ListCreateAPIView):
   # SELECT * FROM categorias
   queryset = CategoriaModel.objects.all() #La consulta que se hara la bd y se mostrara
   serializer_class = CategoriasSerializer #Es la forma en como se mostrara la data

# Endpoint para crear mis categorias
class CreateCategorias(generics.CreateAPIView):
   serializer_class = CategoriasSerializer

class SingleCategoria(generics.RetrieveUpdateDestroyAPIView):
   queryset = CategoriaModel.objects.all()
   serializer_class = CategoriasSerializer

# Reto
# Hacer el CRUD para el modelo Productos Model (views)
# Hacer el serializador para el Producto Model
# No se permita insertar stock negativo
# No se permita insertar stock decimal
# Te devuelva solo los productos que estan en visible True