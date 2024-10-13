from flask import Flask
from settings.db import db
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/db_mail"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '-------'
app.config['MAIL_PASSWORD'] = '----'
app.config['MAIL_DEFAULT_SENDER'] = '-------'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicialización de extensiones
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)  # Inicializa Flask-Mail

# Registrar blueprints

if __name__ == '__main__':
    app.run(debug=True)
