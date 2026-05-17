# Arquitetura da Aplicacao

Este documento descreve o padrao arquitetural utilizado no projeto Flix App.

## Visao Geral

O Flix App segue um padrao de arquitetura em camadas (Layered Architecture) com separacao clara de responsabilidades. Todos os dados vem da [Flix_API](https://github.com/marcosilvaa/flix_api) — a aplicacao nao possui banco de dados local.

1. **Camada de Apresentacao (Page)**
2. **Camada de Servico (Service)**
3. **Camada de Repositorio (Repository)** — comunica-se com a [Flix_API](https://github.com/marcosilvaa/flix_api)

## Camadas

### Camada de Apresentacao (Page)

Localizada nos arquivos `page.py` de cada modulo. Responsavel por:

- Renderizar interfaces com Streamlit (`st.write`, `st.text_input`, `st.button`, etc.)
- Exibir dados tabulares com `AgGrid` do `st_aggrid`
- Coletar entradas do usuario
- Chamar a camada de servico para obter ou persistir dados
- Tratar casos de dados vazios com mensagens de aviso

Convensao de nomenclatura: funcao principal deve se chamar `show_<modulo>()` (ex: `show_genres`, `show_actors`).

```python
# Padrao tipico de uma funcao de pagina
def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()
    if genres:
        genres_df = pd.json_normalize(genres)
        AgGrid(data=genres_df, reload_data=True, key='genres_grid')
    else:
        st.warning("Nenhum genero encontrado!")
```

### Camada de Servico (Service)

Localizada nos arquivos `service.py` (ou `services.py` no modulo movies). Responsavel por:

- Implementar logica de negocio
- Cachear dados em `st.session_state` para evitar chamadas repetidas a API
- Preparar dicionarios de dados antes de enviar ao repositorio
- Delegar chamadas HTTP ao repositorio

```python
class GenreService:
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres
        return genres
```

### Camada de Repositorio (Repository)

Localizada nos arquivos `repository.py` de cada modulo. Responsavel por:

- Fazer chamadas HTTP para a API externa via `requests`
- Configurar headers com token JWT de `st.session_state.token`
- Tratar codigos de resposta: 200/201 (sucesso), 401 (chamar `logout()`), outros (lancar Exception)
- Encapsular URLs e detalhes de comunicacao

```python
class GenreRepository:
    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(self.__genres_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
```

## Modulos da Aplicacao

### `api/` — Autenticacao JWT
- `service.py`: Classe `Auth` que faz POST para `/authentication/token/` com credenciais de usuario.

### `login/` — Login e Logout
- `page.py`: Formulario de login com campos de usuario e senha.
- `service.py`: Funcoes `login()` e `logout()` que gerenciam o token em `st.session_state`.

### `home/` — Dashboard de Estatisticas
- `page.py`: Funcao `show_home()` que exibe graficos Plotly e contadores (filmes por genero, total de filmes, total de avaliacoes, media de estrelas).

### `genres/` — CRUD de Generos
- `page.py`: Listagem com AgGrid + formulario de cadastro com validacao de nome duplicado.
- `service.py`: Classe `GenreService` com cache em session_state.
- `repository.py`: Classe `GenreRepository` com GET e POST para `/genres/`.

### `actors/` — CRUD de Atores
- `page.py`: Listagem com AgGrid + formulario com nome, data de nascimento e nacionalidade.
- `service.py`: Classe `ActorService` com cache em session_state.
- `repository.py`: Classe `ActorRepository` com GET e POST para `/actors/`.

### `movies/` — CRUD de Filmes
- `page.py`: Listagem com AgGrid + formulario com titulo, genero (selectbox), atores (multiselect), data de lancamento e resumo.
- `services.py`: Classe `MovieService` com cache e integracao com GenreService/ActorService. **Nota:** nome de arquivo plural.
- `repository.py`: Classe `MovieRepository` com GET, POST e endpoint de estatisticas (`/movies/stats/`).

### `reviews/` — CRUD de Avaliacoes
- `page.py`: Listagem com AgGrid + formulario com selecao de filme (selectbox), estrelas (number_input 0-5) e comentario.
- `service.py`: Classe `ReviewService` com cache em session_state e integracao com MovieService.
- `repository.py`: Classe `ReviewRepository` com GET e POST para `/reviews/`.

## Fluxo de Autenticacao

1. Ao iniciar, `app.py` verifica se `st.session_state` contem a chave `token`.
2. Se nao houver token, redireciona para `show_login()`.
3. O usuario informa credenciais e clica em Login.
4. `login.service.login()` cria uma instancia de `Auth` e chama `get_token(username, password)`.
5. Em caso de sucesso, o token JWT e armazenado em `st.session_state['token']` e a pagina e recarregada.
6. Em caso de falha, uma mensagem de erro e exibida.
7. Quando qualquer repositorio recebe HTTP 401, chama `logout()` que limpa toda a sessao e redireciona para login.

## Fluxo de Dados Tipico

```
Usuario interage (page.py)
    → Service processa logica de negocio (service.py)
        → Repository faz chamada HTTP (repository.py)
            → API externa responde
        ← Repository retorna dados brutos
    ← Service retorna dados processados/cached
← Page renderiza dados na UI (Streamlit/AgGrid/Plotly)
```

## Cache em Session State

Todos os servicos (GenreService, ActorService, MovieService, ReviewService) implementam cache simples em `st.session_state`:

- Na primeira chamada, buscam dados da API e armazenam em session_state.
- Nas chamadas subsequentes, retornam dados do cache.
- Apos operacoes de criacao (POST), o novo recurso e anexado a lista em cache com `.append()`.

Isso evita chamadas repetidas a API durante a mesma sessao, mas significa que dados podem ficar desatualizados ate que o usuario faca logout/login.