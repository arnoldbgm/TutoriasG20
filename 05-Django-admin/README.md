# Primeros pasos con Django 🦾🐍
[<img src="https://daiderd.com/nix-darwin/images/nix-darwin.png" width="200px" alt="logo" />](https://github.com/LnL7/nix-darwin)
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
pip install django
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
### 6. Crear un superusuario en Django
```bash
python manage.py createsuperuser
```
### 7. Instalacion de UNFOLD
```bash
pip install django-unfold
```
En tu ``core/settings.py``📂, coloca ``unfold`` antes del ``django.contrib.admin``
```py
INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin", 
]
```
### 8. Creacion de una aplicacion
```
python manage.py startapp productos
```
Siempre que tu crees un aplicativo en Django, este debe de ser registrado en el ``core/settings.py``📂
```py
INSTALLED_APPS = [
    'productos'
]
```
### 9. Modelado de la base de datos
![Bd_Django](https://github.com/user-attachments/assets/dece3017-b9dd-4a30-a953-ce5cb6ee4b93)

Si modelas lo siguiente
```py
class CategoriasModel(models.Model):
   nombre = models.CharField(max_length=255)
```
Esto no se vera en tu base de datos hasta que tu ejecutes lo siguiente
```
python manage.py makemigrations
python manage.py migrate
```
### 10. Registrar un modelo en mi admin de Django

```py
# Esto es para unfold
from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(MyModel)
class CustomAdminClass(ModelAdmin):
    pass


# Esto es para Django normal o Jazzmine
from django.contrib import admin
from .models import CategoriasModel, ProductosModel

@admin.register(CategoriasModel)
class CategoriasAdmin(admin.ModelAdmin):
   list_display =  ["nombre"]

@admin.register(ProductosModel)
class ProductoAdmin(admin.ModelAdmin):
   list_display = ["titulo", "stock", "contenido"]
```