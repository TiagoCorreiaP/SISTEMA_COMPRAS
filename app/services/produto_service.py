from sqlalchemy.orm import Session
from app.repositories import produto_repository

def criar_produto(db: Session, nome: str, descricao: str, preco:float):
    if not nome:
        raise Exception("Nome é obrigatório")
    if preco <= 0:
        raise Exception("Preço deve ser maior que zero")
    return produto_repository.criar_produto(db, nome, descricao, preco)

def listar_produtos(db: Session):
    return produto_repository.listar_produtos(db)

def deletar_produto(db: Session, id):
    return produto_repository.deletar_produto(db, id)