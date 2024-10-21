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
### 7. Instalacion de JAZZMINE
```bash
pip install -U django-jazzmin
```
En tu ``core/settings.py``📂, coloca ``jazzim`` antes del ``django.contrib.admin``
```py
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
]
```