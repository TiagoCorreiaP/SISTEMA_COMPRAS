from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    quantidade = Column(Integer)
    status = Column(String(50))