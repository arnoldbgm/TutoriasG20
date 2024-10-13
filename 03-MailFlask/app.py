from flask import Flask
from db import db
from flask_migrate import Migrate
from flask_mail import Mail
from router.usuarios_router import usuario_router

app = Flask(__name__)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:mxhCaUqODasYDGdpZbuTyytktgtxIGXG@junction.proxy.rlwy.net:29578/railway"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'arnold.gallegosm@gmail.com'
app.config['MAIL_PASSWORD'] = 'atwy xgbe vpwt xfal'
app.config['MAIL_DEFAULT_SENDER'] = 'arnold.gallegosm@gmail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicialización de extensiones
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)  # Inicializa Flask-Mail

# Registrar blueprints
app.register_blueprint(usuario_router, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
