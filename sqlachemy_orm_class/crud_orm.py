from conexao import Session
from modelos import Cidade

def criar(nome, pais):

	with Session() as s:

		s.add(Cidade(nome = nome, pais = pais))
		s.commit()

def listar():

	with Session() as s:

		return s.query(Cidade).all()

def deletar_tudo():

	with Session() as s:

		s.query(Cidade).delete()
		s.commit()

