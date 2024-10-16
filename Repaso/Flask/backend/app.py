from flask import Flask
from settings.db import db

app = Flask(__name__)
#Para conectarnos colocamos
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/flask-repaso"
db.init_app(app)

if __name__ == '__main__':
   app.run(debug=True)