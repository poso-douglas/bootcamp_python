from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///banco_desafio.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

resultado = (
    session.query(Fornecedor.nome.func.sum(Produto.preco).label("total_preco"))
    .join(Produto, Fornecedor.id == Produto.fornecedor.id)
    .group_by(Fornecedor.nome)
    .all()
)

for nome, total_preco in resultado:
    print(f"{nome},{total_preco}")
