from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Criando a conexão
engine = create_engine("sqlite:///meubanco.db", echo=False)

print("Conexão criada com sucesso!")

Base = declarative_base()


# Classe que representa a tabela usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


# Criar a tabela
Base.metadata.create_all(engine)

# Cria sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo registros na tabela usuarios
novo_usuario = Usuario(nome="Douglas", idade=38)
session.add(novo_usuario)
session.commit()

# print("Usuario incluido com sucesso!")


# Consultando dados
usuario = session.query(Usuario).filter_by(nome="Douglas").first()
print(f"{usuario.id} - {usuario.nome} - {usuario.idade}")

usuario = session.query(Usuario).all()
for id, nome, idade in usuario:
    print(f"{id} - {nome} - {idade}")

# with Session() as sess:
#     usuario = Usuario(nome="Griselda", idade=43)
#     sess.add(usuario)

# print(f"{usuario.id} - {usuario.nome} - {usuario.idade}")
