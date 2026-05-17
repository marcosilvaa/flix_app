# Modulo de Filmes

O modulo de filmes e responsavel pelo cadastro, listagem e estatisticas de filmes na aplicacao Flix App, integrando informacoes de generos e atores.

## Visao Geral

O modulo de filmes gerencia:
- Listagem de filmes cadastrados com informacoes detalhadas
- Cadastro de novos filmes com associacao a generos e atores
- Estatisticas de filmes via dashboard (consumido pelo modulo home)
- Exibicao de dados em formato tabular com AgGrid

## Estrutura do Modulo

```
movies/
├── __init__.py
├── page.py        # Interface de usuario para filmes
├── repository.py  # Camada de comunicacao com a API (MovieRepository)
└── services.py    # Logica de negocio (MovieService) — nome plural
```

**Atencao**: O arquivo de servico usa nome plural `services.py`, diferente dos demais modulos que usam `service.py` (singular). Importar como `movies.service` causara `ModuleNotFoundError`.

## Componentes

### page.py

- **Funcao**: `show_movies()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de filmes
- **Dependencias**: `movies.services.MovieService`, `genres.service.GenreService`, `actors.service.ActorService`
- **Caracteristicas**:
  - Exibe lista de filmes em formato tabular com AgGrid
  - Remove coluna `actors` do DataFrame antes de exibir (`movies_df.drop(columns=['actors'])`)
  - Formulario para cadastro de novos filmes com campos:
    - Titulo do filme (text_input)
    - Selecao de genero (selectbox com generos da API)
    - Selecao multipla de atores (multiselect com atores da API)
    - Data de lancamento (date_input com validacao: 1800 ate hoje, formato DD/MM/YYYY)
    - Resumo do filme (text_area)
  - Tratamento de casos vazios com mensagem de aviso
  - Feedback de sucesso ou erro apos cadastro

### services.py

- **Classe**: `MovieService`
- **Responsabilidade**: Implementar a logica de negocio para filmes
- **Metodos**:
  - `get_movies()`: Busca filmes da API com cache em `st.session_state.movies`
  - `create_movie(title, genre, actors, release_date, resume)`: Prepara dict e envia ao repositorio; adiciona ao cache apos criacao
  - `get_movie_stats()`: Retorna estatisticas agregadas (filmes por genero, total, avaliacoes, media de estrelas)

### repository.py

- **Classe**: `MovieRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operacoes de filmes
- **Metodos**:
  - `get_movies()`: GET para `http://localhost:8000/api/v1/movies/`
  - `create_movie(movie)`: POST para o mesmo endpoint
  - `get_movie_stats()`: GET para `http://localhost:8000/api/v1/movies/stats/`
- **Tratamento de respostas HTTP** (200, 201, 401, outros lancam Exception)
- **Atencao**: No metodo `get_movie_stats()`, o tratamento de 401 nao retorna `None` (diferente dos outros metodos) — apenas chama `logout()` sem retornar valor explicito

## Funcionalidades

### Listagem de Filmes

- Busca filmes via `MovieService` com cache em session_state
- Exibe em tabela AgGrid com key `movies_grid`
- Coluna `actors` e removida do DataFrame para facilitar a leitura
- Tratamento de caso vazio com `st.warning()`

### Cadastro de Filmes

- Formulario com validacoes de dados (datas, campos obrigatorios)
- Selecao de genero: dropdown com mapeamento `nome:id` dos generos disponiveis
- Selecao multipla de atores: multiselect com mapeamento `nome:id`
- Data de lancamento: intervalo de 01/01/1800 ate hoje
- Feedback visual de sucesso ou erro
- Recarregamento automatico via `st.rerun()` apos cadastro bem-sucedido

### Estatisticas de Filmes

- Metodo `get_movie_stats()` disponivel em `MovieService`
- Consumido pelo modulo `home/` para exibir dashboard
- Retorna: filmes por genero, total de filmes, total de avaliacoes, media de estrelas

## Integracao com Outros Modulos

### Modulo de Generos

- Importacao de `GenreService` para obtencao da lista de generos
- Mapeamento `nome:id` para selectbox de genero no formulario

### Modulo de Atores

- Importacao de `ActorService` para obtencao da lista de atores
- Mapeamento `nome:id` para multiselect de atores no formulario

### Modulo Home

- `home/page.py` importa `MovieService` para chamar `get_movie_stats()`
- Os dados de estatisticas sao usados para graficos Plotly e contadores

## Padroes de Codigo

- Funcao de pagina segue padrao `show_<modulo>()`
- Servico implementa injecao de dependencia do repositorio
- Repositorio encapsula URLs e headers de autenticacao
- Tratamento consistente de erros HTTP
- Normalizacao de dados com `pd.json_normalize()` para exibicao no AgGrid
- Cache em `st.session_state` para evitar chamadas repetidas