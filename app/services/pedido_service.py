from app import models
from sqlalchemy.orm import Session

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

def criar_pedido(db: Session, pedido):
    novo = models.Pedido(**pedido.dict())

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo

def listar_pedidos(db: Session):
    return db.query(models.Pedido).all()