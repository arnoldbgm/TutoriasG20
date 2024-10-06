# Primero llamamos al archivo db.py
from settings.db import db
from sqlalchemy import (Column, String, Integer, Float)


class CategoriasModel(db.Model):
    __tablename__ = 'categorias'

