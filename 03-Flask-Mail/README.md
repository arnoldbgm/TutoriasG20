Aquí tienes un ejemplo de un archivo `README.md` que explica cómo configurar y enviar correos electrónicos en tu proyecto Flask utilizando Flask-Mail:

```markdown
# Proyecto Flask - Envío de Correos Electrónicos

Este proyecto Flask está configurado para enviar correos electrónicos utilizando Flask-Mail. A continuación, se detallan los pasos para configurar y enviar correos electrónicos en la aplicación.

## Requisitos

- Flask
- Flask-Mail
- Flask-Bcrypt
- Flask-SQLAlchemy
- Otros requisitos específicos del proyecto

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Crea un entorno virtual**:

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de Flask-Mail

1. **Configuración en `app.py`**:

   Asegúrate de que `app.py` esté configurado para usar Flask-Mail. Aquí está la configuración básica:

   ```python
   from flask import Flask
   from flask_mail import Mail

   app = Flask(__name__)

   # Configuración de Flask-Mail
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USERNAME'] = '<TU_EMAIL>'
   app.config['MAIL_PASSWORD'] = '<TU_CONTRASEÑA>'
   app.config['MAIL_DEFAULT_SENDER'] = '<TU_EMAIL>'
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USE_SSL'] = False

   # Inicialización de Flask-Mail
   mail = Mail(app)
   ```

2. **Archivo HTML para el correo**:

   Coloca el archivo HTML del correo en la carpeta `templates`. Por ejemplo, `welcome_email.html`:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Bienvenido</title>
   </head>
   <body>
       <h1>Hola {{ username }}</h1>
       <p>Gracias por registrarte en nuestra aplicación. ¡Esperamos que disfrutes de tu experiencia!</p>
   </body>
   </html>
   ```

## Envío de Correos Electrónicos

1. **Función para enviar correos**:

   En el archivo `utils/email_utils.py`, define la función `send_welcome_email` para enviar correos electrónicos:

   ```python
   from flask_mail import Message
   from flask import render_template

   def send_welcome_email(to_email, username):
       from app import mail  # Importación tardía para evitar ciclos
       msg = Message('Bienvenido a nuestra aplicación', recipients=[to_email])
       msg.html = render_template('welcome_email.html', username=username)
       mail.send(msg)
   ```

2. **Uso de la función en `usuarios_router.py`**:

   En tu archivo de enrutamiento (por ejemplo, `router/usuarios_router.py`), llama a la función `send_welcome_email` después de registrar un nuevo usuario:

   ```python
   from flask import Blueprint, request, jsonify
   from models.usuarios_model import UsuarioModel
   from db import db
   from flask_bcrypt import Bcrypt
   from utils.email_utils import send_welcome_email

   bcrypt = Bcrypt()

   usuario_router = Blueprint('usuario_router', __name__)

   @usuario_router.route('/register', methods=['POST'])
   def register():
       data = request.get_json()

       # Validar si el usuario ya existe
       if UsuarioModel.query.filter_by(username=data['username']).first() or UsuarioModel.query.filter_by(email=data['email']).first():
           return jsonify({"message": "Usuario o correo electrónico ya registrado"}), 400

       # Hashing de la contraseña
       hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

       # Crear un nuevo usuario
       new_user = UsuarioModel(username=data['username'], email=data['email'], password=hashed_password)

       # Guardar en la base de datos
       db.session.add(new_user)
       db.session.commit()

       # Enviar correo de bienvenida
       send_welcome_email(new_user.email, new_user.username)

       return jsonify({"message": "Usuario registrado con éxito"}), 201
   ```

## Ejecución

1. **Ejecuta la aplicación**:

   ```bash
   python app.py
   ```

2. **Prueba el registro de usuarios**:

   Realiza una solicitud POST a `/api/v1/register` con los datos del usuario para probar el envío de correos electrónicos.

## Notas

- Asegúrate de reemplazar `<TU_EMAIL>` y `<TU_CONTRASEÑA>` con tus credenciales de correo electrónico.
- La configuración de `MAIL_SERVER` puede necesitar ajustes dependiendo del proveedor de correo electrónico que uses.

---
