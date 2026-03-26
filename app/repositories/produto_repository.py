from sqlalchemy.orm import Session
import app.models as models

def criar_produto(db: Session, nome: str, descricao: str):
    produto = models.Produto(nome=nome, descricao=descricao)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def listar_produtos(db: Session):
    return db.query(models.Produto).all()