from settings.db import db
from datetime import datetime
from sqlalchemy import (Column, String, Integer, ForeignKey, Text, DateTime)


class PostModel(db.Model):
    __tablename__ = 'posts'

