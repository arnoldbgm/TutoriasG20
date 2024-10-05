# Primero llamamos al archivo db.py
from settings.db import db
from sqlalchemy import (Column, String, Integer, Float)


class CategoriasModel(db.Model):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)