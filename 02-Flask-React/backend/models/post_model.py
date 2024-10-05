from settings.db import db
from datetime import datetime
from sqlalchemy import (Column, String, Integer, ForeignKey, Text, DateTime)


class PostModel(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    titulo = Column(String, nullable=False)
    contenido = Column(Text, nullable=False)
    categoria_id = Column
    product_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
