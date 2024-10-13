from settings.db import db
from datetime import datetime
from sqlalchemy import (Column, 
                        String, 
                        Integer)


class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)