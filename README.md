# MatriXplore

<img src="app/static/img/LOGO.png" alt="MatriXplore Logo" width="200">

MatriXplore é uma aplicação web desenvolvida em Python com FastAPI para o processamento e análise de matrizes, conjuntos e relações. Esta aplicação permite aos usuários carregar arquivos CSV contendo dados de matrizes ou inserir esses dados manualmente. Com base nos dados fornecidos, a aplicação analisa propriedades matemáticas das matrizes, como funcionalidade, injetividade, totalidade, entre outras.

## Funcionalidades

- **Carregar Arquivos CSV**: Faça o upload de arquivos CSV contendo matrizes e relações para análise.
- **Inserção Manual**: Insira matrizes, conjuntos e relações manualmente para análise instantânea.
- **Propriedades Matemáticas**: Analisa propriedades matemáticas das matrizes, como funcionalidade, injetividade, totalidade, sobrejetividade, entre outras.
- **Download de Arquivos**: Baixe arquivos CSV de matrizes pré-configuradas para testes.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/MatriXplore.git
   cd MatriXplore
   ```
2. Clone este repositório:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
## Uso

1. Inicie o servidor FastAPI:

    ```bash 
    uvicorn app.main:app --reload --port 8001
    ```
2. Abra o navegador e acesse:

    ```bash 
    http://127.0.0.1:8001
    ```
3. Navegue pelas seguintes páginas para utilizar as funcionalidades da aplicação:

    **Home**: Página inicial com informações sobre a aplicação.
    **Upload de Matrizes**: Faça o upload de arquivos CSV para análise.
    **Inserção Manual**: Insira dados manualmente para análise imediata.
    **Bases de Matrizes**: Acesse matrizes disponíveis para download.

## Estrutura do Projeto
-    **app/main.py**: Contém a lógica principal do servidor FastAPI.
-    **app/utils.py**: Implementa as funções de processamento e análise de matrizes.
-    **app/templates/**: Armazena os arquivos HTML para renderização das páginas.
-    **app/static/**: Contém arquivos estáticos, como CSS e imagens.
-    **requirements.txt**: Lista das dependências do projeto.

## Exemplo de Formato de Arquivo CSV

- Para processar matrizes corretamente, os arquivos CSV devem estar estruturados da seguinte maneira:
    
    ```bash
    # MATRIZES
    Matriz, R
    1, 0, 0, 0
    0, 1, 0, 0
    0, 0, 1, 0
    0, 0, 0, 1

    Matriz, S
    0, 1, 0
    1, 0, 1
    0, 1, 0

    # CONJUNTOS
    Conjunto, A, 1, 2, 3, 4
    Conjunto, B, a, b, c, d, e

    # RELAÇÕES
    Relação, R, (1, a), (2, c), (3, d)
    Relação, S, (a, x), (c, y), (d, z)

    ```
## Tecnologias Utilizadas

-    **FastAPI**: Framework para construir APIs rápidas e eficientes.
-    **Jinja2**: Engine de templates para renderizar HTML.
-    **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
-    **Numpy**: Biblioteca para computação científica em Python.

## Estrutura de Diretórios
- **Diretórios**
    ```bash
    MatriXplore/
    │
    ├── app/
    │   ├── main.py                # Lógica principal do FastAPI
    │   ├── utils.py               # Funções de processamento de matrizes
    │   ├── templates/             # Páginas HTML
    │   └── static/                # Arquivos estáticos (CSS, JS, Imagens)
    │
    ├── base-test/                 # Diretório com arquivos CSV para download
    ├── requirements.txt           # Lista de dependências do projeto
    └── README.md                  # Documentação do projeto

    ```
