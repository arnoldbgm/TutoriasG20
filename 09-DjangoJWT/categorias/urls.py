from django.urls import path
from .views import *

urlpatterns = [
   path('categorias/', CreateCategorias.as_view() )
]