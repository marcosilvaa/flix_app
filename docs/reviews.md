# Modulo de Avaliacoes

O modulo de avaliacoes e responsavel pela listagem e cadastro de avaliacoes de filmes na aplicacao Flix App, com integracao completa com a API externa.

## Visao Geral

O modulo de avaliacoes gerencia:
- Listagem de avaliacoes cadastradas via API
- Cadastro de novas avaliacoes vinculadas a filmes
- Selecao de filme via dropdown com dados da API
- Validacao de estrelas (0 a 5)
- Exibicao de dados em formato tabular com AgGrid

## Estrutura do Modulo

```
reviews/
├── __init__.py
├── page.py         # Interface de usuario para avaliacoes
├── service.py      # Logica de negocio (ReviewService)
└── repository.py   # Camada de comunicacao com a API (ReviewRepository)
```

## Componentes

### page.py

- **Funcao**: `show_reviews()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de avaliacoes
- **Dependencias**: `reviews.service.ReviewService`, `movies.services.MovieService`
- **Caracteristicas**:
  - Exibe lista de avaliacoes em formato tabular com AgGrid
  - Formulario para cadastro de nova avaliacao com:
    - Selecao de filme via `st.selectbox` (mapeamento titulo:id)
    - Estrelas via `st.number_input` (0 a 5, step 1)
    - Comentario via `st.text_area`
  - Feedback de sucesso ou erro apos cadastro
  - Recarregamento automatico da pagina apos cadastro bem-sucedido
- **Problema conhecido**: Variavel nomeada `revies_service` na linha 9 — typo, deveria ser `reviews_service`

### service.py

- **Classe**: `ReviewService`
- **Responsabilidade**: Implementar a logica de negocio para avaliacoes
- **Caracteristicas**:
  - Metodo `get_reviews()`: Busca avaliacoes com cache em `st.session_state`
  - Metodo `create_review(movie, stars, comment)`: Prepara dados e envia ao repositorio
  - Adiciona nova avaliacao ao cache apos criacao bem-sucedida
  - Integracao com `ReviewRepository` para comunicacao com a API

### repository.py

- **Classe**: `ReviewRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operacoes de avaliacoes
- **Caracteristicas**:
  - URL: `http://localhost:8000/api/v1/reviews/`
  - Headers com token JWT de `st.session_state.token`
  - Metodo `get_reviews()`: GET para listar avaliacoes
  - Metodo `create_review(review)`: POST para criar avaliacao
  - Tratamento de respostas HTTP (200, 201, 401)
  - Chamada a `logout()` em caso de falha de autenticacao (401)

## Funcionalidades

### Listagem de Avaliacoes

- Busca avaliacoes da API via `ReviewService`
- Exibe em tabela interativa com AgGrid (key `movies_grid`)
- Tratamento de caso vazio com `st.warning()`

### Cadastro de Avaliacoes

- Selecao de filme: busca lista de filmes via `MovieService`, cria mapeamento `titulo:id`
- Estrelas: inteiro de 0 a 5
- Comentario: texto livre
- Apos cadastro bem-sucedido, recarrega a pagina com `st.rerun()`

## Integracao com MovieService

O formulario de avaliacao importa `MovieService` de `movies.services` para:
1. Obter a lista de filmes disponiveis
2. Criar um dicionario mapeando `titulo -> id`
3. Permitir selecao do filme pelo titulo no `st.selectbox`
4. Enviar o ID do filme ao criar a avaliacao

## Fluxo de Dados

```
show_reviews()
  → ReviewService.get_reviews()
    → ReviewRepository.get_reviews()
      → GET /api/v1/reviews/
  → MovieService.get_movies()
    → MovieRepository.get_movies()
      → GET /api/v1/movies/
  → ReviewService.create_review(movie, stars, comment)
    → ReviewRepository.create_review(review)
      → POST /api/v1/reviews/
```

## Padroes de Codigo

- Funcao de pagina segue padrao `show_<modulo>()`
- Servico implementa injecao de dependencia do repositorio
- Repositorio encapsula URLs e headers de autenticacao
- Normalizacao de dados com `pd.json_normalize()` para exibicao no AgGrid
- Cache de avaliacoes em `st.session_state.reviews`
- Uso de `st.rerun()` para atualizar a interface apos cadastro