# Modulo de Atores

O modulo de atores e responsavel pelo cadastro e listagem de atores na aplicacao Flix App, permitindo o gerenciamento de informacoes de elenco para associacao com filmes.

## Visao Geral

O modulo de atores gerencia:
- Listagem de atores cadastrados via API
- Cadastro de novos atores com nome, data de nascimento e nacionalidade
- Cache de dados em sessao do Streamlit
- Exibicao de dados em formato tabular com AgGrid

## Estrutura do Modulo

```
actors/
├── __init__.py
├── page.py        # Interface de usuario para atores (show_actors)
├── service.py     # Logica de negocio (ActorService)
└── repository.py  # Comunicacao com a API (ActorRepository)
```

## Componentes

### page.py

- **Funcao**: `show_actors()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de atores
- **Caracteristicas**:
  - Exibe lista de atores em formato tabular com AgGrid (key `actors_grid`)
  - AgGrid com opcoes: `columns_auto_size_mode=True`, `enableSorting=True`, `enableFilter=True`, `enableColResize=True`
  - Formulario para cadastro de novos atores com campos:
    - Nome do ator (text_input)
    - Data de nascimento (date_input: min 01/01/1900, max hoje, formato DD/MM/YYYY)
    - Nacionalidade (selectbox: opcoes fixas `BRAZIL`, `USA`)
  - Tratamento de casos vazios com `st.warning()`
  - Feedback de sucesso ou erro apos cadastro
  - Recarregamento automatico via `st.rerun()`
- **Problema conhecido**: Variavel nomeada `actor_serivce` na linha 9 — typo, deveria ser `actor_service`

### service.py

- **Classe**: `ActorService`
- **Responsabilidade**: Implementar a logica de negocio para atores
- **Metodos**:
  - `get_actors()`: Busca atores com cache em `st.session_state.actors`
  - `create_actor(name, birthday, nationality)`: Cria dict `{'name': name, 'birthdate': birthday, 'nationality': nationality}`, envia ao repositorio e adiciona ao cache
- **Injecao de dependencia**: `ActorRepository` instanciado no `__init__`
- **Bug conhecido**: No metodo `create_actor()`, linha 24, `return actor` retorna o dict de entrada em vez de `return new_actor` (resposta da API)

### repository.py

- **Classe**: `ActorRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operacoes de atores
- **URL**: `http://localhost:8000/api/v1/actors/`
- **Headers**: `Authorization: Bearer {token}` de `st.session_state.token`
- **Metodos**:
  - `get_actors()`: GET para listar atores (status 200 → JSON, 401 → logout, outros → Exception)
  - `create_actor(actor)`: POST para criar ator (status 201 → JSON, 401 → logout, outros → Exception)

## Funcionalidades

### Listagem de Atores

- Busca atores via `ActorService` com cache em session_state
- Exibe em tabela AgGrid com ordenacao, filtragem e redimensionamento de colunas
- Tratamento de caso vazio com `st.warning("Nenhum Ator/Atriz encontrado")`

### Cadastro de Atores

- Campo de texto para nome
- Date input com intervalo de 01/01/1900 ate hoje (formato DD/MM/YYYY)
- Selectbox de nacionalidade com opcoes fixas: `BRAZIL` e `USA`
- Feedback de sucesso: `st.success(f"Ator '{name}' cadastrado com sucesso!")`
- Recarregamento via `st.rerun()`

## Integracao com Outros Modulos

### Modulo de Filmes

- `movies/page.py` importa `ActorService` para obter lista de atores
- Cria mapeamento `nome:id` para multiselect de atores no formulario de filme
- Permite associacao multipla de atores ao elenco de um filme

## Bugs Conhecidos

| Arquivo | Linha | Descricao |
|---------|-------|-----------|
| `actors/page.py` | 9 | Variavel `actor_serivce` — typo, deveria ser `actor_service` |
| `actors/service.py` | 24 | `return actor` retorna o dict de entrada em vez de `return new_actor` (resposta da API) |

## Padroes de Codigo

- Funcao de pagina segue padrao `show_<modulo>()`
- Servico implementa injecao de dependencia do repositorio
- Repositorio encapsula URLs e headers de autenticacao
- Tratamento consistente de erros HTTP
- Normalizacao de dados com `pd.json_normalize()` para exibicao no AgGrid
- Cache em `st.session_state` para evitar chamadas repetidas