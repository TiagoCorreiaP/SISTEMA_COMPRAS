from app import models

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

def criar_pedido(db, produto_id, fornecedor_id, quantidade):
    pedido = models.Pedido(
        produto_id=produto_id,
        fornecedor_id=fornecedor_id,
        quantidade=quantidade,
        status="criado"
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido

def criar_pedido(db, produto_id, fornecedor_id, quantidade):
    pedido = models.Pedido(
        produto_id=produto_id,
        fornecedor_id=fornecedor_id,
        quantidade=quantidade,
        status="criado"
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido