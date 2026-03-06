# 🌍 European Cities CRUD - SQLAlchemy (ORM vs Core)

Este projeto demonstra a implementação de um sistema CRUD (Create, Read, Update, Delete) utilizando Python e **SQLAlchemy 2.0**. O diferencial técnico deste repositório é a coexistência de duas abordagens de persistência no mesmo ecossistema: **ORM (Object-Relational Mapping)** e **Core (SQL Expression Language)**.

## 🚀 Tecnologias Utilizadas
*   **Python 3.x**
*   **SQLAlchemy 2.0**: O kit de ferramentas SQL mais versátil para Python.
*   **SQLite**: Banco de dados relacional leve e embutido.

## 🏗️ Arquitetura do Projeto
O projeto foi desenvolvido seguindo princípios de **Separação de Responsabilidades (SoC)**, dividindo a aplicação em camadas lógicas:

1.  **`conexao.py`**: Configuração central da `Engine` e das sessões do banco de dados.

2.  **`modelos.py`**: Definição da estrutura de dados utilizando classes ORM (`DeclarativeBase`).

3.  **`tabelas.py`**: Definição da estrutura de dados utilizando objetos de tabela (Core).

4.  **`crud_orm.py`**: Lógica de manipulação de dados utilizando a abstração de classes.

5.  **`crud_core.py`**: Lógica de manipulação de dados utilizando comandos SQL programáticos.

6.  **`main.py`**: Interface de linha de comando (CLI) interativa que permite ao usuário escolher o motor de execução.

## 💡 Funcionalidades
*   **Escolha de Motor**: O usuário pode decidir no início da execução se deseja operar via ORM ou Core.

*   **Interface Interativa**: Menu amigável para cadastro, listagem e exclusão de cidades.

*   **Persistência Efêmera**: Implementação de uma política de limpeza que apaga todos os registros ao encerrar o programa, garantindo um ambiente de teste sempre limpo.

*   **Gestão de Contexto**: Uso rigoroso de `with Session()` e `with engine.connect()` para garantir o fechamento correto das conexões e evitar vazamentos de memória.

## 🛠️ Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com

### 🛠️ Instalação Rápida
1. Recomenda-se criar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou: venv\Scripts\activate  # Windows

2. Instale as dependências automaticamente:

   pip install -r requirements.txt

### 💡 Dica de Especialista:

Como você está usando o **SQLAlchemy 2.0**, você pode gerar o arquivo requirements.txt automaticamente com as versões exatas que você usou na sua máquina rodando este comando no terminal:

pip freeze > requirements.txt`

Isso garante que o projeto nunca "quebre" por causa de uma atualização futura da biblioteca, pois fixa a versão exata que você testou.

## 🛡️ Boas Práticas e Segurança
Neste projeto, foram aplicadas diretrizes fundamentais para o desenvolvimento de software robusto:
*   **Prevenção de SQL Injection**: O uso do `SQLAlchemy Core` e `ORM` garante que todos os parâmetros sejam tratados de forma segura (parameterized queries), impedindo ataques de injeção de SQL.
*   **Gerenciamento de Contexto (Context Managers)**: Utilização sistemática do `with Session()` e `with engine.connect()`, garantindo que as conexões sejam fechadas automaticamente, mesmo em caso de falhas críticas.
*   **Segregação de Responsabilidades**: A lógica de interface (CLI) nunca acessa o banco de dados diretamente; ela depende exclusivamente da camada de serviço (`crud_*.py`), facilitando a manutenção e testes unitários.

## 🚀 Próximos Passos (Roadmap)
Para evoluir este projeto, as seguintes implementações são planejadas:

1.  **Migração de Banco de Dados**: Alterar o `engine` para suportar bancos de produção como **PostgreSQL** ou **MySQL** apenas trocando a string de conexão.

2.  **Validação de Dados**: Integrar a biblioteca **Pydantic** para validar os campos (ex: impedir nomes de cidades vazios) antes de chegarem à camada de persistência.

3.  **Interface Web**: Evoluir o `main.py` para uma API REST utilizando **FastAPI**, aproveitando a estrutura assíncrona do SQLAlchemy 2.0.

4.  **Migrations**: Implementar o **Alembic** para gerenciar versões do banco de dados de forma profissional, permitindo alterações na estrutura das tabelas sem perda de dados.


Instale as dependências:

pip install sqlalchemy

Execute a aplicação:

python main.py
python main_old.py
python main_CORE_ORM.py (Este último com a escolha de executar com CORE ou ORM)

🧠 Aprendizados Relevantes

   - Diferença ORM vs Core: Entendimento prático de quando usar abstrações de classes (ORM) para produtividade ou expressões SQL (Core) para performance e controle granular.
   
   - Modularização: Organização de arquivos para facilitar a manutenção e escalabilidade do código.
    
   - Tratamento de Erros: Gestão de exceções como OperationalError e ciclo de vida de tabelas no SQLite.

Desenvolvido por Renato Mendes