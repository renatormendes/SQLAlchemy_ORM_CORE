# 
# Escolha um dos dois para importar:
# from crud_orm import criar, listar, deletar_tudo
# from crud_core import criar, listar, deletar_tudo
# 

from crud_orm import criar, listar, deletar_tudo

if __name__ == "__main__":

	try:

		criar("Lisboa", "Portugal")
		criar("Rio de Janeiro", "Brasil")
		criar("Tóquio", "Japão")
		criar("Kremilin", "Rússia")

		cidades = listar()

		for c in cidades:

			print(f"ID: {c.id} | Nome: {c.nome} | País: {c.pais}")

	finally:

		deletar_tudo()

