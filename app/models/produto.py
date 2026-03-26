from sqlalchemy import Column, Integer, String, ForeignKey
from app.models import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String)