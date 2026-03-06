import sqlalchemy as db
from conexao import engine
from tabelas import tabela_cidades

def criar(nome, pais):

	with engine.connect() as conn:

		conn.execute(db.insert(tabela_cidades).values(nome = nome, pais = pais))
		conn.commit()

def listar():

	with engine.connect() as conn:

		return conn.execute(db.select(tabela_cidades)).fetchall()

def deletar_tudo():

	with engine.connect() as conn:

		conn.execute(db.delete(tabela_cidades))
		conn.commit()