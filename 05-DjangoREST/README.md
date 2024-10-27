# Primeros pasos con Django REST framework 🦾🐍
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
### 8. Creacion de una aplicacion
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
