# Esta es la instancia de mi SQLAlchemy
from settings.db import db
from sqlalchemy import Column, Integer, String, Text, DateTime

# Porque db.Model? 
# Estamos herando las propiedades de SQLAlchemy
# Para crear mis tablas
class PostModel(db.Model):
   # __table__ sirve para nombrar nuestra tabla
   __tablename__ = 'posts'

   # Column(TipodelDato, opciones)
   id = Column(Integer, primary_key=True)
   titulo = Column(String(255))
   contenido = Column(Text)
   fecha = Column(DateTime)
