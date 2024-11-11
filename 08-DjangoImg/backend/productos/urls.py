from django.urls import path
from .views import *

urlpatterns = [
   path('categorias/', ListCreateCategorias.as_view())
]