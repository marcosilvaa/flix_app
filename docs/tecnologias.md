# Tecnologias Utilizadas

Este documento lista as tecnologias, frameworks e bibliotecas utilizados no projeto Flix App.

## Dependencias Principais

As dependencias estao definidas no `pyproject.toml`:

| Pacote | Versao | Funcao |
|--------|--------|--------|
| Python | >=3.14 | Linguagem de programacao |
| Streamlit | >=1.52.1 | Framework web para interface grafica |
| requests | >=2.32.5 | Chamadas HTTP a API externa |
| streamlit-aggrid | >=1.2.1 | Tabelas interativas (AgGrid) |
| plotly | >=6.5.0 | Graficos e visualizacoes (dashboard Home) |
| flake8 | >=7.3.0 | Linter (tambem e dependencia de desenvolvimento) |

## Dependencias de Desenvolvimento

| Pacote | Versao | Funcao |
|--------|--------|--------|
| flake8 | 7.3.0 | Linter de codigo Python |

Configuracao do flake8 em `.flake8`: ignora regra E501 (linhas longas), exclui diretorio `.venv`.

## Bibliotecas Transistivas Relevantes

| Pacote | Funcao |
|--------|--------|
| pandas | Manipulacao e normalizacao de dados (`pd.json_normalize()`) |
| numpy | Calculo numerico (dependencia do pandas e plotly) |

## Gerenciamento de Pacotes

O projeto utiliza **uv** como gerenciador de pacotes:

- `pyproject.toml` — Declaracao de dependencias e metadados do projeto
- `uv.lock` — Lock file para reprodutibilidade
- `uv sync` — Instala dependencias conforme o lock file
- `uv run streamlit run app.py` — Executa a aplicacao
- `uv run flake8 .` — Executa o linter

Os arquivos `requirements.txt` e `requirements_dev.txt` sao exportacoes geradas por `uv export` e nao devem ser editados manualmente.

## Framework e Bibliotecas

### Streamlit

- Framework principal para a interface web
- Gerencia o estado da aplicacao via `st.session_state`
- Fornece componentes de UI: inputs, botoes, selectbox, multiselect, date_input, text_area
- Roteamento baseado em `st.sidebar.selectbox` no `app.py`
- Recarregamento automatico via `st.rerun()` apos operacoes de escrita

### Pandas

- Usado exclusivamente para `pd.json_normalize()` — converte listas de dicts JSON em DataFrames para o AgGrid
- Nao e usado para manipulacao de dados alem da normalizacao

### Requests

- Biblioteca para todas as chamadas HTTP a API externa
- Usado nos repositorios com metodos `requests.get()` e `requests.post()`
- Autenticacao via header `Authorization: Bearer <token>`

### Streamlit-AgGrid

- Componente para exibicao de dados em tabelas interativas
- Parametros comuns: `data`, `key`, `reload_data`/`reload`, `columns_auto_size_mode`, `enableSorting`, `enableFilter`, `enableColResize`
- Nao e usado para edicao de dados — apenas exibicao

### Plotly

- Usado no modulo `home/` para graficos de estatisticas
- `plotly.express.pie()` para grafico de pizza de filmes por genero
- Exibido via `st.plotly_chart()`

### Datetime

- Biblioteca padrao do Python para manipulacao de datas
- Usado no modulo `actors/` e `movies/` para inputs de data com validacao de range

## API Externa

| Propriedade | Valor |
|-------------|-------|
| Repositorio | [https://github.com/marcosilvaa/flix_api](https://github.com/marcosilvaa/flix_api) |
| URL base | `http://localhost:8000/api/v1/` |
| Protocolo | REST API |
| Autenticacao | JWT (JSON Web Tokens) |
| Formato | JSON |
| Endpoints | `/authentication/token/`, `/genres/`, `/actors/`, `/movies/`, `/movies/stats/`, `/reviews/` |

## Configuracao

| Arquivo | Conteudo |
|---------|----------|
| `config.toml` | `app_title = 'Flix App'` (nao e lido pelo codigo) |
| `.flake8` | Exclui `.venv`, ignora E501 |
| `.python-version` | `3.14` |
| `.gitignore` | `__pycache__/`, `*.py[oc]`, `build/`, `dist/`, `wheels/`, `*.egg-info`, `.venv` |