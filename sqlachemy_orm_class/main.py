import sys
import os
from crud_orm import criar, listar, deletar_tudo

def menu():
    while True:

        print("\n" + "="*30)
        print("🌍 GERENCIADOR DE CIDADES")
        print("="*30)
        print("1. Cadastrar nova cidade")
        print("2. Listar todas as cidades")
        print("3. Sair e Limpar Banco")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            nome = input("Digite o nome da cidade: ")
            pais = input("Digite o país: ")
            criar(nome, pais)
            print(f"\n✅ {nome} adicionada com sucesso!")

        elif opcao == "2":

            cidades = listar()
            print("\n--- CIDADES CADASTRADAS ---")

            if not cidades:

                print("Nenhum registro encontrado.")

            else:

                for c in cidades:

                    # Se for ORM, acessamos como c.nome. Se for Core, c['nome'] ou c.nome.
                    print(f"ID: {c.id} | Cidade: {c.nome} | País: {c.pais}")

        elif opcao == "3":

            print("\n🧹 Limpando dados e encerrando...")
            deletar_tudo()
            print("Até logo!")
            break
        
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    
    menu()
