from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from conexao import engine # Importe a engine aqui
Base = declarative_base()

class Cidade(Base):

	__tablename__ = 'cidades_orm'
	id = Column(
			Integer, 
			primary_key = True, 
			autoincrement = True
		)
	nome = Column(String)
	pais = Column(String)


# ADICIONE ISSO: Garante que a tabela exista antes de qualquer CRUD
Base.metadata.create_all(engine)

