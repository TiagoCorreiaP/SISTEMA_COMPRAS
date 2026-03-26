from app import models

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