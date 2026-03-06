from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from tabelas import metadata

# Configuração da Engine
engine = create_engine("sqlite:///european_database.sqlite")

# ESSE COMANDO É ESSENCIAL: ele lê o metadata e cria as tabelas no arquivo .sqlite
metadata.create_all(engine)

# Base para o ORM
Base = declarative_base()

# Definição do Modelo
class Cidade(Base):

	__tablename__ = 'cidades'

	id = Column(Integer, primary_key = True, autoincrement = True)
	nome = Column(String, nullable = False)
	pais = Column(String, nullable = False)

# Cria as tabelas
Base.metadata.create_all(engine)

# Coniguração da Sessão
Session = sessionmaker(bind = engine)