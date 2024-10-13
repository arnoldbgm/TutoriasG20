from settings.db import db
from datetime import datetime
from sqlalchemy import (Column, 
                        String, 
                        Integer)


class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'