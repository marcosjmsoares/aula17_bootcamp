from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# insert no banco
# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# novo_usuario = Usuario(nome='João', idade=28)
# session.add(novo_usuario)
# session.commit()

# print("Usuário inserido com sucesso.")

#consulta banco de dados
# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# usuario = session.query(Usuario).filter_by(nome='João').first()
# print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")


from sqlalchemy.orm import sessionmaker
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
#session = Session()

with Session.begin() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    
