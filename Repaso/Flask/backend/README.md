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


### 3. Instalar Flask y todo lo del proyecto 🛠️

```bash
pip install Flask
```

### 4. Crear un archivo `app.py` 📄

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

if __name__ == '__main__':
    app.run(debug=True)

```

### 5. Ejecutar la aplicación ▶️

```bash
python app.py

```
### 6. Crearemos las carpetas
A continuacion crearemos las carpetas `controllers` `router` `settings` `models` 📂

### 7. Instalacion de SQLAlchemy, PsyCop
Esto me permitira conectarme a mi bd y crear tablas

```bash
pip install Flask-SQLAlchemy
```
```bash
pip install psycopg2
```

### 8. Crear el archivo `settings/db.py` 📂

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

### 7. Conectar a una base de datos con Flask-SQLAlchemy 🔗

```python
from flask import Flask
from settings.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'Aqui_va_tu_bd'

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

```

### 8. Creacion de la base de datos
![image](https://github.com/user-attachments/assets/f69a535b-f8f1-4c3b-a065-4b8f518a9f85)

### 9. Ejecutar la migración 🚀

- **Crear la carpeta `migrations` (Solo la primera vez)**:
    
    ```bash
    flask db init
    
    ```
    
- **Crear la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db migrate -m "0001-Creacion de BD"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    
    ```
    

### 10. Pasamos a crear las rutas para nuestra bd🚀

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```
