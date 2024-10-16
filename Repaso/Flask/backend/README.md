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

### 9. Crearemos  el archivo `models/posts_model.py` 📂
Aqui vamos a crear la tabla posts

```py
# Esta es la instancia de mi SQLAlchemy
from settings.db import db
from sqlalchemy import Column, Integer, String, Text, DateTime

class PostModel(db.Model):
   # __table__ sirve para nombrar nuestra tabla
   __tablename__ = 'posts'

   # Column(TipodelDato, opciones)
   id = Column(Integer, primary_key=True)
   titulo = Column(String(255))
   contenido = Column(Text)
   fecha = Column(DateTime)
```
### 10. Migrar mis tablas creadas a mi bd
Haremos la migracion de las tablas a mi bd
```bash
pip install Flask-Migrate
```
Añadiremos lo siguiente al `app.py`
```py
from flask_migrate import Migrate
#Recuerda que debes de importar a tu tabla, sino no se vera la migracion
from models import posts_models
...
migrate = Migrate(app, db)
```
### 11. Ejecutar la migración 🚀

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
    
### 12. Pasamos a crear las rutas para nuestra API usando Flask-restx🚀
Instalaremos Flask-restx
```bash
pip install flask-restx
```
Dentro de tu archivo `app.py`
```py
from flask_restx import Api
...
api = Api(app)
```
Crearemos el archivo ``router/posts_router.py``
```py
#Debemos de importar a flask_rest (Namespace)
from flask_restx import Namespace, Resource

#Agrupar todas las rutas

api = Namespace('api')

@api.route('/listar-post')
class PostList(Resource):
   def get(self):
      return "Hola mundo"
```
Ahora llamamos al ``posts_router.py`` desde mi ``app.py``

```py
from router.posts_router import api as post_ns
...
# Se registra las rutas de la siguiente forma
api.add_namespace(post_ns)
```
El endpoint al final se vera de esta manera 
```bash
http://127.0.0.1:5000/api/listar-post
```

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```
