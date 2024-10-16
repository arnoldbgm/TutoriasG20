from flask_restx import Namespace, Resource
from flask import request, jsonify
# Estoy importando los modelos
from models.posts_models import PostModel
from settings.db import db

api = Namespace('v1', description='Rutas relacionadas con los posts')


@api.route('/listar-post')
class PostList(Resource):
    def post(self):
        """Creamos los posts"""
        # Siempre debes de llamar al request de flask
        body = request.json
        new_post = PostModel(**body)
        # Para añadir debes de usar el (add) y guardar (commit)
        db.session.add(new_post)
        db.session.commit()
        # Siempre debes de dar una respuesta JSON
        return jsonify({
            'message': 'Post creado exitosamente 👍',
            'id': new_post.id,
            'titulo': new_post.titulo,
            'fecha': new_post.fecha
        })

    def get(self):
        posts = PostModel.query.all()
        return jsonify([
            {
                # Es el formato de como vamos a devolver la infromacion
                "id": post.id,
                "fecha": post.fecha,
                "titulo": post.titulo,
                "contenido": post.contenido
            }
            for post in posts])
