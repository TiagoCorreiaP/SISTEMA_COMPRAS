from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.models import Base
from sqlalchemy.orm import relationship

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    quantidade = Column(Integer)
    status = Column(String, default="criado")
    total = Column(Float)

    produto = relationship("Produto")
    fornecedor = relationship("Fornecedor")
    