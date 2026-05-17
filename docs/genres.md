# Modulo de Generos

O modulo de generos e responsavel pelo cadastro e listagem de generos na aplicacao Flix App, permitindo a categorizacao de filmes.

## Visao Geral

O modulo de generos gerencia:
- Listagem de generos cadastrados via API
- Cadastro de novos generos com nome descritivo
- Validacao de nome vazio e nome duplicado (case-insensitive)
- Cache de dados em sessao do Streamlit
- Exibicao de dados em formato tabular com AgGrid

## Estrutura do Modulo

```
genres/
├── __init__.py
├── page.py        # Interface de usuario para generos (show_genres)
├── service.py     # Logica de negocio (GenreService)
└── repository.py  # Comunicacao com a API (GenreRepository)
```

## Componentes

### page.py

- **Funcao**: `show_genres()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de generos
- **Caracteristicas**:
  - Exibe lista de generos em formato tabular com AgGrid (key `genres_grid`)
  - Formulario para cadastro de novo genero com campo de nome
  - Validacao de nome vazio com mensagem de erro
  - Validacao de nome duplicado (case-insensitive) — **Nota**: bug na linha 30, `g['name'].lower` sem parenteses, deveria ser `.lower()`
  - Feedback de sucesso ou erro apos cadastro
  - Recarregamento automatico via `st.rerun()` apos cadastro bem-sucedido

### service.py

- **Classe**: `GenreService`
- **Responsabilidade**: Implementar a logica de negocio para generos
- **Metodos**:
  - `get_genres()`: Busca generos com cache em `st.session_state.genres`
  - `create_genre(name)`: Cria dict `{'name': name}`, envia ao repositorio e adiciona ao cache
- **Injecao de dependencia**: `GenreRepository` instanciado no `__init__`

### repository.py

- **Classe**: `GenreRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operacoes de generos
- **URL**: `http://localhost:8000/api/v1/genres/`
- **Headers**: `Authorization: Bearer {token}` de `st.session_state.token`
- **Metodos**:
  - `get_genres()`: GET para listar generos (status 200 → JSON, 401 → logout, outros → Exception)
  - `create_genre(genre)`: POST para criar genero (status 201 → JSON, 401 → logout, outros → Exception)

## Funcionalidades

### Listagem de Generos

- Busca generos via `GenreService` com cache em session_state
- Exibe em tabela AgGrid com `reload_data=True`
- Tratamento de caso vazio com `st.warning("Nenhum genero encontrado!")`

### Cadastro de Generos

- Campo de texto para nome do genero
- Validacao: nome vazio → `st.error("O campo nome nao pode estar vazio.")`
- Validacao: nome duplicado → `st.error('O genero "{name}" ja existe!')`
- Feedback de sucesso: `st.success(f'Genero: {name} cadastrado com sucesso!')`
- Recarregamento via `st.rerun()`

## Integracao com Outros Modulos

### Modulo de Filmes

- `movies/page.py` importa `GenreService` para obter lista de generos
- Cria mapeamento `nome:id` para selectbox de genero no formulario de filme

## Bug Conhecido

Na linha 30 de `genres/page.py`, a validacao de nome duplicado usa:
```python
existing_genres = {g['name'].lower for g in genres}
```
O acesso `g['name'].lower` retorna o metodo bound em vez de chamá-lo. Deveria ser:
```python
existing_genres = {g['name'].lower() for g in genres}
```

## Padroes de Codigo

- Funcao de pagina segue padrao `show_<modulo>()`
- Servico implementa injecao de dependencia do repositorio
- Repositorio encapsula URLs e headers de autenticacao
- Tratamento consistente de erros HTTP
- Normalizacao de dados com `pd.json_normalize()` para exibicao no AgGrid
- Cache em `st.session_state` para evitar chamadas repetidas