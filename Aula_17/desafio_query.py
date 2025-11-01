from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from desafio import Produto, Fornecedor


engine = create_engine('sqlite:///desafio.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

resultado = (session.query(
                Fornecedor.nome,
                func.sum(Produto.preco).label('total_preco')
            )
            .join(Produto, Fornecedor.id == Produto.fornecedor_id)
            .group_by(Fornecedor.nome).all())

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")