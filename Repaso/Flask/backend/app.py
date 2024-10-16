from flask import Flask
from settings.db import db
from flask_migrate import Migrate
from models import posts_models
from flask_restx import Api
# Traigo a todos los rutas del namespace
from router.posts_router import api as post_ns
from flask_cors import CORS

app = Flask(__name__)
#Para conectarnos colocamos
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/flask-repaso"
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app , prefix='/api') # Añadimos este prefijo
CORS(app)

# Se registra las rutas de la siguiente forma
api.add_namespace(post_ns)

if __name__ == '__main__':
   app.run(debug=True)