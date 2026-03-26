from fastapi import FastAPI
from app.database import engine
from app.models import Base

from app.routes import fornecedor, produto, pedido, usuario

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(fornecedor.router)
app.include_router(produto.router)
app.include_router(pedido.router)
app.include_router(usuario.router)