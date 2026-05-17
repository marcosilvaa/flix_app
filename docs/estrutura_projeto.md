# Estrutura do Projeto

Esta secao descreve a organizacao dos arquivos e pastas do projeto Flix App.

## Visao Geral

```
flix_app/
├── app.py              # Ponto de entrada da aplicacao Streamlit
├── main.py             # Stub obsoleto (nao utilizar)
├── pyproject.toml      # Configuracao do projeto e dependencias
├── uv.lock             # Lock file do gerenciador de pacotes uv
├── config.toml         # Configuracao da aplicacao (titulo)
├── .flake8             # Configuracao do linter flake8
├── .python-version     # Versao do Python (3.14)
├── .gitignore          # Arquivos ignorados pelo Git
├── requirements.txt    # Dependencias exportadas (gerado por uv)
├── requirements_dev.txt # Dependencias de desenvolvimento
├── api/                # Modulo de autenticacao JWT
│   ├── __init__.py
│   └── service.py      # Classe Auth para obtensao de tokens
├── login/              # Modulo de autenticacao de usuarios
│   ├── __init__.py
│   ├── page.py         # Interface de login (show_login)
│   └── service.py      # Funcoes login() e logout()
├── home/               # Modulo de dashboard
│   ├── __init__.py
│   └── page.py         # Dashboard com estatisticas (show_home)
├── genres/             # Modulo de generos (CRUD completo)
│   ├── __init__.py
│   ├── page.py         # Interface de listagem e cadastro
│   ├── service.py      # Logica de negocio (GenreService)
│   └── repository.py   # Chamadas a API (GenreRepository)
├── actors/             # Modulo de atores (CRUD completo)
│   ├── __init__.py
│   ├── page.py         # Interface de listagem e cadastro
│   ├── service.py      # Logica de negocio (ActorService)
│   └── repository.py   # Chamadas a API (ActorRepository)
├── movies/             # Modulo de filmes (CRUD + estatisticas)
│   ├── __init__.py
│   ├── page.py         # Interface de listagem e cadastro
│   ├── services.py     # Logica de negocio (MovieService) — nome plural
│   └── repository.py   # Chamadas a API (MovieRepository + stats)
├── reviews/            # Modulo de avaliacoes (CRUD completo)
│   ├── __init__.py
│   ├── page.py         # Interface de listagem e cadastro
│   ├── service.py      # Logica de negocio (ReviewService)
│   └── repository.py   # Chamadas a API (ReviewRepository)
└── docs/               # Documentacao do projeto
    ├── README.md
    ├── arquitetura.md
    ├── estrutura_projeto.md
    ├── padroes_codigo.md
    ├── tecnologias.md
    ├── api.md
    ├── login.md
    ├── home.md
    ├── genres.md
    ├── actors.md
    ├── movies.md
    └── reviews.md
```

## Arquivos na Raiz

| Arquivo | Responsabilidade |
|---------|-----------------|
| `app.py` | Ponto de entrada real da aplicacao. Verifica `st.session_state.token` e roteia para login ou menu lateral. |
| `main.py` | Stub obsoleto com `print("Hello from flix-app!")`. Nao e usado pela aplicacao. |
| `pyproject.toml` | Define o projeto (`flix-app`), versao do Python (>=3.14) e dependencias (streamlit, requests, streamlit-aggrid, plotly, flake8). |
| `uv.lock` | Lock file gerenciado pelo `uv` para versoes deterministicas de dependencias. |
| `config.toml` | Apenas `app_title = 'Flix App'`. Atualmente nao e lido pelo codigo da aplicacao. |
| `.flake8` | Configuracao do linter: ignora E501 (linha longa), exclui `.venv`. |
| `.python-version` | Fixa a versao do Python em `3.14`. |
| `requirements.txt` | Exportacao de dependencias gerada por `uv export`. Nao editar manualmente. |
| `requirements_dev.txt` | Dependencias de desenvolvimento: apenas `flake8==7.3.0`. |

## Descricao das Pastas

- **`api/`**: Servico de autenticacao JWT. Contem apenas `service.py` com a classe `Auth` que faz POST para `/authentication/token/`. Nao possui page nem repository.
- **`login/`**: Interface e logica de autenticacao. `page.py` com formulario de login, `service.py` com funcoes `login()` e `logout()`. Nao usa classes, usa funcoes.
- **`home/`**: Dashboard de estatisticas. Apenas `page.py` com graficos Plotly (pizza de filmes por genero) e contadores (total de filmes, avaliacoes, media de estrelas).
- **`genres/`**: CRUD completo de generos. segue o padrao page/service/repository com classes.
- **`actors/`**: CRUD completo de atores. Segue o padrao page/service/repository com classes.
- **`movies/`**: CRUD de filmes mais endpoint de estatisticas. Usa o nome plural `services.py` (diferente dos demais modulos). Integracao com GenreService e ActorService para formularios.
- **`reviews/`**: CRUD completo de avaliacoes. Integracao com MovieService para listagem de filmes no formulario.
- **`docs/`**: Documentacao do projeto em Markdown.

## Atencao

- O arquivo `main.py` e um stub do `uv init` e nao faz parte da aplicacao. O ponto de entrada real e `app.py`.
- O modulo `movies/` usa o nome de arquivo `services.py` (plural), enquanto todos os outros usam `service.py` (singular). Importar como `movies.service` causara erro.