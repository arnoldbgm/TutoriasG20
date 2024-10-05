from flask import Flask
from settings.db import db 
from flask_migrate import Migrate
# Para que te reconzca la bd debes de importarlo de esta forma 🐍
from models import (
    categoria_model,
    post_model
)
from router.product_router import product_router

app = Flask(__name__)
# Aqui va las credenciales de mi bd
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/db_pos"

# Aqui le digo que cuanto inicie mi app, que se haga la migracion si es que hay
db.init_app(app)
migrate = Migrate(app, db)

# Aqui es donde voy a crear mi ruta
app.register_blueprint(product_router, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
