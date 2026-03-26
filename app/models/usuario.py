from sqlalchemy import Column, Integer, String, ForeignKey
from app.models import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    senha = Column(String(255))