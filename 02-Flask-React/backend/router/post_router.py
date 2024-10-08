from flask import Blueprint, request, jsonify
from models.post_model import PostModel
from settings.db import db

post_router = Blueprint('post_router', __name__)

# Vamos a crear una ruta, que diga hola mundo
# @(el nombre de la variable del Blueprint).route('/nombre_endpoitn', methods=['GET'])

# GET => TRAER
# POST => INSERTAR - CREAR
# DELETE => ELIMINAR
# PUT-PATCH => ACTUALIZAR

@post_router.route('/posts', methods=['POST'])
def create_post():
   # Para crear algo, debemos enviar informacion
   # Debemos de importar (request) flask
   data = request.get_json()
   # {
   #  "fecha": "2024-12-25",
   #  "titulo": "Una aventura unica",
   #  "contenido": "Este es un ejemplo del contenido"
   # }
   # Debemos darle el formato a la data - debes importar el modelo
   # nuevo_post = PostModel(fecha=data.get('fecha'), titulo=data.get('titulo'), contenido=data.get('contendio'))
   nuevo_post = PostModel(**data) #kwargs
   #Insertar esto en la base de datos
   db.session.add(nuevo_post)
   #Siempre se debe confirmar para el caso POST PUT DELETE
   db.session.commit()
   #Las respuestas se deben de retornar en json
   # Yo debo de importar un jsonify
   return jsonify({
      'message': 'Post creado exitosamente 👍',
      'id': nuevo_post.id,
      'titulo': nuevo_post.titulo,
   })
   