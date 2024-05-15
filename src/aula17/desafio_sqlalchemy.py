from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    telefone = Column(String(20))
    email = Column(String(30))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    descricao = Column(String(50))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    fornecedor = relationship("Fornecedor")


engine = create_engine("sqlite:///banco_desafio.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fornecedores = [
    Fornecedor(
        nome="Forncedor A",
        telefone="1199999999",
        email="contato@fornecedor.com",
        endereco="Rua a n10",
    ),
    Fornecedor(
        nome="Forncedor B",
        telefone="1199999999",
        email="contato@fornecedor.com",
        endereco="Rua a n10",
    ),
    Fornecedor(
        nome="Forncedor C",
        telefone="1199999999",
        email="contato@fornecedor.com",
        endereco="Rua a n10",
    ),
    Fornecedor(
        nome="Forncedor D",
        telefone="1199999999",
        email="contato@fornecedor.com",
        endereco="Rua a n10",
    ),
]

produtos = [
    Produto(
        nome="Produto A", descricao="Descricao produto", preco=100, fornecedor_id=1
    ),
    Produto(
        nome="Produto B", descricao="Descricao produto", preco=200, fornecedor_id=2
    ),
    Produto(
        nome="Produto C", descricao="Descricao produto", preco=300, fornecedor_id=3
    ),
    Produto(
        nome="Produto D", descricao="Descricao produto", preco=650, fornecedor_id=4
    ),
]

# session.add_all(fornecedores)
# session.add_all(produtos)
# session.commit()

# for produto in session.query(Produto).all():
#     print(f"{produto.nome},- {produto.fornecedor.nome}")


resultado = (
    session.query(Fornecedor.nome.func.sum(Produto.preco).label("total_preco"))
    .join(Produto, Fornecedor.id == Produto.fornecedor.id)
    .group_by(Fornecedor.nome)
    .all()
)

for nome, total_preco in resultado:
    print(f"{nome},{total_preco}")
