from sqlalchemy.orm import Session
import app.models as models
from app.models.produto import Produto
def criar_produto(db: Session, nome: str, descricao: str, preco:float):
    produto = models.Produto(nome=nome, descricao=descricao, preco=preco)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def listar_produtos(db: Session):
    return db.query(models.Produto).all()

def deletar_produto(db: Session, id):
    produto = db.query(Produto).filter(Produto.id == id).first()
    db.delete(produto)
    db.commit()
    return None