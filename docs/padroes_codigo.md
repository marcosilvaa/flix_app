# Padroes de Codigo

Esta secao descreve as diretrizes de estilo e boas praticas adotadas no projeto Flix App, incluindo convencoes observadas e advertencias sobre problemas conhecidos.

## Convencoes de Nomenclatura

| Elemento | Convensao | Exemplo |
|----------|-----------|---------|
| Variaveis e funcoes | `snake_case` | `get_genres`, `movie_title` |
| Classes | `PascalCase` | `GenreService`, `MovieRepository` |
| Constantes | `UPPER_SNAKE_CASE` | `BASE_URL`, `MAX_RETRIES` |
| Funcoes de pagina | Prefixo `show_` | `show_genres`, `show_actors` |
| Atributos privados | Prefixo duplo `__` | `self.__base_url`, `self.__headers` |

## Importacoes

Ordem recomendada:

1. Bibliotecas padrao do Python (ex: `datetime`)
2. Bibliotecas de terceiros (`streamlit`, `pandas`, `requests`, `st_aggrid`, `plotly`)
3. Modulos do projeto (`genres.service`, `login.service`, etc.)

```python
from datetime import datetime

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests

from genres.service import GenreService
from actors.service import ActorService
```

## Estrutura de Funcoes e Classes

### Funcoes de Pagina

Funcoes de pagina devem seguir o padrao `show_<modulo>()` e incluir:

1. Instanciacao do service correspondente
2. Chamada ao metodo de listagem
3. Verificacao de dados vazios com `st.warning()`
4. Normalizacao com `pd.json_normalize()` antes de passar ao AgGrid
5. Formulario de cadastro com validacao e feedback

### Classes de Servico

- Nome: `<Modulo>Service`
- `__init__` instancia o repositorio correspondente
- Implementa cache em `st.session_state` para evitar chamadas repetidas
- Metodos de criacao empacotam dados em `dict()` antes de enviar ao repositorio

### Classes de Repositorio

- Nome: `<Modulo>Repository`
- `__init__` configura `__base_url`, `__<modulo>_url` e `__headers` com token
- Metodos GET retornam `response.json()` para status 200, chamam `logout()` para 401
- Metodos POST retornam `response.json()` para status 201, chamam `logout()` para 401
- Outros status codes lancam `Exception`

## Gerenciamento de Sessao

Chaves de `st.session_state` usadas pela aplicacao:

| Chave | Conteudo |
|-------|----------|
| `token` | Token JWT de autenticacao (string) |
| `genres` | Lista de generos em cache (lista) |
| `actors` | Lista de atores em cache (lista) |
| `movies` | Lista de filmes em cache (lista) |
| `reviews` | Lista de avaliacoes em cache (lista) |

## Tratamento de Erros HTTP

| Codigo | Acao |
|--------|------|
| 200 | Sucesso em GET — retorna `response.json()` |
| 201 | Sucesso em POST — retorna `response.json()` |
| 401 | Token invalido/expirado — chama `logout()` e retorna `None` |
| Outros | Lanca `Exception` com mensagem contendo o status code |

## Data Normalization

Todos os dados de listagem sao convertidos com `pd.json_normalize(data)` antes de serem exibidos no AgGrid. Isso achata estruturas JSON aninhadas em colunas planas para a tabela.

## Problemas Conhecidos no Codigo

### Typos e Bugs

| Arquivo | Linha | Problema |
|---------|-------|----------|
| `actors/page.py` | 9 | Variavel `actor_serivce` — typo, deveria ser `actor_service` |
| `reviews/page.py` | 9 | Variavel `revies_service` — typo, deveria ser `reviews_service` |
| `genres/page.py` | 30 | `g['name'].lower` sem parenteses — deveria ser `g['name'].lower()` |
| `actors/service.py` | 24 | `return actor` retorna o dict de entrada em vez de `return new_actor` (resposta da API) |

### Inconsistencia de Nomenclatura

- O modulo `movies/` usa o nome de arquivo `services.py` (plural), enquanto todos os outros modulos usam `service.py` (singular). Importar como `movies.service` causara `ModuleNotFoundError`.

### Modulo Home sem Service/Repository

- O modulo `home/` so possui `page.py` e importa `MovieService` diretamente de `movies.services`. Nao segue o padrao de tres camadas dos outros modulos.

## Boas Praticas Observadas

1. **Separacao de responsabilidades**: Cada camada (page, service, repository) tem funcoes bem definidas
2. **Encapsulamento**: Atributos privados com prefixo `__` e metodos bem definidos
3. **Cache em sessao**: Evita chamadas repetidas a API
4. **Normalizacao de dados**: Uso consistente de `pd.json_normalize()`
5. **Tratamento de sessao vazia**: Verificacao de dados nulos/vazios antes da exibicao
6. **Feedback ao usuario**: Mensagens claras de sucesso (`st.success`) e erro (`st.error`)
7. **Logout automatico**: Em caso de token invalido (401), a sessao e limpa automaticamente