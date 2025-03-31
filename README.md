# Encurtador de URL

Este projeto é um encurtador de URLs desenvolvido em Python. Ele foi criado com o objetivo de fixar o conhecimento adquirido em FastAPI e SQLAlchemy, proporcionando uma aplicação prática para consolidar esses aprendizados. Além disso, foi implementado seguindo o padrão de projeto **MVC** (Model-View-Controller), garantindo uma melhor organização e separação de responsabilidades no código. O projeto também conta com autenticação **JWT**, utilizando a biblioteca **python-jose** para gerenciar tokens de acesso.

## Estrutura do Projeto

- `app/`: Diretório principal contendo o código-fonte do aplicativo.
  - `models/`: Contém as definições das classes que representam o banco de dados utilizando SQLAlchemy.
  - `controllers/`: Gerencia a comunicação entre as rotas e os serviços, aplicando a lógica de controle.
  - `services/`: Contém a lógica de negócio da aplicação.
  - `views/`: Contém as definições das rotas da API utilizando FastAPI.
  - `core/`: Contém configurações e utilitários essenciais para o funcionamento do sistema.
  - `static/`: Diretório para arquivos estáticos como CSS, JavaScript e imagens.
  - `templates/`: Contém os arquivos HTML utilizados na renderização das páginas.
  - `database.py`: Configuração da conexão com o banco de dados.
  - `main.py`: Arquivo principal que inicia o aplicativo.
- `venv/`: Ambiente virtual para gerenciamento das dependências do projeto.
- `.gitignore`: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no desenvolvimento do projeto.
- **FastAPI**: Framework utilizado para construção da API.
- **SQLAlchemy**: Biblioteca ORM utilizada para interação com o banco de dados.
- **python-jose**: Biblioteca utilizada para autenticação JWT.
- **C++**, **C**, **PowerShell**, **Cython**, **HTML**: Outras linguagens presentes no projeto, conforme indicado pelas estatísticas do GitHub.

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Tomazbr9/Encurtador-de-URL.git
   ```
2. **Navegue até o diretório do projeto**:
   ```bash
   cd Encurtador-de-URL
   ```
3. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux ou macOS:
     ```bash
     source venv/bin/activate
     ```
4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute o aplicativo**:
   ```bash
   python app/main.py
   ```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode fazer isso através de *pull requests* ou abrindo *issues* para relatar problemas e sugerir melhorias.
