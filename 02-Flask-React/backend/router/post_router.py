from flask import Blueprint

post_router = Blueprint('post_router', __name__)

# Vamos a crear una ruta, que diga hola mundo
# @(el nombre de la variable del Blueprint).route('/nombre_endpoitn', methods=['GET'])

# GET => TRAER
# POST => INSERTAR - CREAR
# DELETE => ELIMINAR
# PUT-PATCH => ACTUALIZAR

@post_router.route('/posts', methods=['POST'])
def create_post():
   return "Hola mundo"
