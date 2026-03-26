from app import models
from sqlalchemy.orm import Session
from fastapi import HTTPException

STATUS_PERMITIDOS = [
    "criado",
    "aprovado",
    "comprado",
    "entregue",
    "finalizado",
    "cancelado"
]

TRANSICOES = {
    "criado": ["aprovado", "cancelado"],
    "aprovado": ["comprado", "cancelado"],
    "comprado": ["entregue"],
    "entregue": ["finalizado"],
    "finalizado": [],
    "cancelado": []
}

from app import models
from fastapi import HTTPException

def criar_pedido(db, pedido):

    produto = db.query(models.Produto).filter(
        models.Produto.id == pedido.produto_id
    ).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    fornecedor = db.query(models.Fornecedor).filter(
        models.Fornecedor.id == pedido.fornecedor_id
    ).first()

    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

    total = produto.preco * pedido.quantidade

    novo_pedido = models.Pedido(
        produto_id=pedido.produto_id,
        fornecedor_id=pedido.fornecedor_id,
        quantidade=pedido.quantidade,
        status="criado",
        total=total
    )

    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    return novo_pedido

def listar_pedidos(db: Session):
    return db.query(models.Pedido).all()