from sqlalchemy.orm import Session
from app.repositories import produto_repository

def criar_produto(db: Session, nome: str, descricao: str):
    if not nome:
        raise Exception("Nome é obrigatório")

    return produto_repository.criar_produto(db, nome, descricao)

def listar_produtos(db: Session):
    return produto_repository.listar_produtos(db)


