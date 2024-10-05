from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.categoria_model import CategoriasModel
from models.post_model import PostModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from settings.db import db

from sqlalchemy import func  # Esto se usa para el uso de funciones especificas de SQL

product_router = Blueprint('product_router', __name__)


@product_router.route('/products', methods=['GET'])
def get_products():
    return "Hola mundo"