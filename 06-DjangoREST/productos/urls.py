from django.urls import path
from .views import ListCategorias, CreateCategorias, SingleCategoria

urlpatterns = [
   path('categorias/', ListCategorias.as_view()),
   path('create/', CreateCategorias.as_view()),
   path('categorias/<int:pk>/', SingleCategoria.as_view())
]