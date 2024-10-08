from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.categoria_model import CategoriasModel
from models.post_model import PostModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from settings.db import db

from sqlalchemy import func  # Esto se usa para el uso de funciones especificas de SQL

categoria_router = Blueprint('categoria_router', __name__)


@categoria_router.route('/products', methods=['GET'])
def get_products():
    return ([
        {
            "fecha": "2024-10-04T20:35:07.804Z",
            "titulo": "Toby Wolf MD",
            "contenido": "Beatae laudantium corporis vitae reiciendis nemo tenetur. Voluptatem iusto ipsum. Totam delectus maiores quis. Ducimus hic tempore ex iste modi veniam dicta sequi.",
            "id": "1"
        },
        {
            "fecha": "2024-10-04T10:52:46.409Z",
            "titulo": "Lucy Franecki",
            "contenido": "deserunt omnis fuga",
            "id": "2"
        }
    ])
