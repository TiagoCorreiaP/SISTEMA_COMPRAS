from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .usuario import Usuario
from .produto import Produto
from .fornecedor import Fornecedor
from .pedido import Pedido