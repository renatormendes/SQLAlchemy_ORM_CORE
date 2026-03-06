import sys
import crud_orm
import crud_core

def escolher_modo():
    print("="*30)
    print("   ESCOLHA O MODO DE OPERAÇÃO")
    print("="*30)
    print("1. Usar SQLAlchemy ORM (Classes)")
    print("2. Usar SQLAlchemy CORE (Tabelas)")
    
    escolha = input("Selecione (1 ou 2): ")
    return crud_orm if escolha == "1" else crud_core

def menu():
    # Define qual módulo CRUD será usado para esta sessão
    dao = escolher_modo()
    modo_nome = "ORM" if dao == crud_orm else "CORE"
    
    while True:
        print(f"\n--- 🌍 SISTEMA ({modo_nome}) ---")
        print("1. Cadastrar Cidade")
        print("2. Listar Cidades")
        print("3. Sair (e apagar tudo)")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da cidade: ")
            pais = input("País: ")
            dao.criar(nome, pais)
            print(f"✅ Adicionado via {modo_nome}!")

        elif opcao == "2":
            cidades = dao.listar()
            print(f"\n--- LISTA DE CIDADES ({modo_nome}) ---")
            for c in cidades:
                # O SQLAlchemy Core retorna Row, o ORM retorna Objetos. 
                # Ambos permitem acesso via .nome e .pais
                print(f"ID: {c.id} | Nome: {c.nome} | País: {c.pais}")

        elif opcao == "3":
            dao.deletar_tudo()
            print(f"🧹 Banco limpo via {modo_nome}. Saindo...")
            break
        
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu()
