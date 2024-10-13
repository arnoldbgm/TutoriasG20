from db import db
from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from models.usuarios_model import UsuarioModel
from utils.email_utils import send_welcome_email  # Importa la función desde utils

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
