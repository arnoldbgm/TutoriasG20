# DRF + JWT 🦾🐍
<img src="https://github.com/user-attachments/assets/07230e79-3fdc-48bc-84f4-60e6fdd32063" alt="imagen" style="width: 400px;" />

### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv

```

### 2. Activar el entorno virtual ⚡
- En Windows:
    ```bash
        venv\Scripts\activate
    ```
- En gitbash:
    ```
        source venv/Scripts/activate
    ```
- En macOS y Linux:
    ```bash
        source venv/bin/activate
    ```


### 3. Instalacion de Django
```bash
pip install django djangorestframework
```
### 4. Crear un proyecto en Django
Con este comando crearemos nuestro primer proyecto en Django
```bash
django-admin startproject core .
```
### 5. Como levantar mi proyecto de Django
```bash
python manage.py migrate
python manage.py runserver
```
### 6. Creacion de una aplicacion
```
python manage.py startapp productos
```
Siempre que tu crees un aplicativo en Django, este debe de ser registrado en el ``core/settings.py``📂
```py
INSTALLED_APPS = [
    'rest_framework',
    'productos'
]
```
### 9. Modelado de la base de datos

![Bd_Django](https://github.com/user-attachments/assets/dece3017-b9dd-4a30-a953-ce5cb6ee4b93)

### 10. Creacion de los serializadores
El serializador que permite deserealizar la data, validar la data y especificar que se va enviar o mostrar al cliente

Nostros debemos de crear el archivo ``serializers.py``📂
```py
from rest_framework import serializers
from .models import CategoriaModel

# Este sera un serializador para Categorias
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['categoria']
```
### 11. Creacion de los views
Crearemos un view de tipo get para poder listar las categorias
```py
from rest_framework import generics
from .models import CategoriaModel
from .serializers import CategoriasSerializer

# Endpoint para mostrar todas las categorias
class ListCategorias(generics.ListAPIView):
   # SELECT * FROM categorias
   queryset = CategoriaModel.objects.all() #La consulta que se hara la bd y se mostrara
   serializer_class = CategoriasSerializer #Es la forma en como se mostrara la data
```
### 12. Creacion de las URLS
Crearemos las urls asociandolas a un view
```py
from django.urls import path
from .views import ListCategorias

urlpatterns = [
   path('categorias/', ListCategorias.as_view())
]
```

### 13. Configuracion para mostrar imagenes locales en Django

```py

# Configuración en urls.py para servir archivos de medios en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```