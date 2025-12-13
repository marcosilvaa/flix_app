# Padrões de Código

Esta seção descreve as diretrizes de estilo e boas práticas adotadas no projeto Flix App.

## Estilo de Código

### Convenções de Nomenclatura

- **Variáveis e funções**: `snake_case` (ex: `get_user_info`, `movie_title`)
- **Classes**: `PascalCase` (ex: `GenreService`, `MovieRepository`)
- **Constantes**: `UPPER_SNAKE_CASE` (ex: `BASE_URL`, `MAX_RETRIES`)
- **Funções de página**: Devem iniciar com o prefixo `show_` (ex: `show_genres`, `show_actors`)
- **Atributos privados**: Usar prefixo duplo sublinhado `__` (ex: `self.__base_url`)

### Importações

As importações seguem a ordem recomendada:

1. Bibliotecas padrão do Python (datetime, etc.)
2. Bibliotecas de terceiros (streamlit, pandas, requests, st_aggrid)
3. Módulos do projeto (genres.service, actors.service, etc.)

```python
from datetime import datetime
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests
from genres.service import GenreService
from actors.service import ActorService
```

## Estrutura de Funções e Classes

### Funções de Página

Funções de página devem seguir o padrão `show_nome_modulo` e incluir:

- Exibição de dados com AgGrid quando aplicável
- Mensagens claras para o usuário
- Tratamento de casos vazios
- Formulários para criação de novos registros

```python
def show_actors():
    actor_service = ActorService()  # Instanciação do serviço correspondente
    actors = actor_service.get_actors()  # Obtenção dos dados

    if actors:  # Verificação se há dados
        st.write("Lista de Atores")
        actors_df = pd.json_normalize(actors)  # Normalização para exibição
        AgGrid(
            data=actors_df,
            key='actors_grid',
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
        )
    else:
        st.warning("Nenhum Ator/Atriz encontrado")

    # Formulário de criação
    st.title("Cadastrar novo Ator")
    name = st.text_input('Nome do ator')
    # ... restante do formulário
```

### Classes de Serviço

Classes seguem o padrão `NomeModuloService` com:

- Método `__init__` que instancia o repositório correspondente
- Métodos que implementam lógica de negócios
- Preparação de dados para comunicação com o repositório

```python
class ActorService:
    def __init__(self):
        self.actor_repository = ActorRepository()  # Injeção de dependência

    def get_actors(self):
        return self.actor_repository.get_actors()  # Delegação ao repositório

    def create_actor(self, name, birthday, nationality):
        # Preparação dos dados antes de enviar ao repositório
        actor = dict(
            name=name,
            birthdate=birthday,
            nationality=nationality,
        )
        return self.actor_repository.create_actor(actor)
```

### Classes de Repositório

Classes seguem o padrão `NomeModuloRepository` com:

- Método `__init__` que configura URL base e headers de autenticação
- Métodos que fazem chamadas HTTP para a API externa
- Tratamento de respostas (200, 201, 401) e erros
- Encapsulamento de detalhes de comunicação com a API

```python
class ActorRepository:
    def __init__(self):
        self.__base_url = 'https://marcosilva.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'  # URL específica do módulo
        self.__headers = {
            'Authorization': f"Bearer {st.session_state.token}"  # Token de autenticação
        }

    def get_actors(self):
        response = requests.get(self.__actors_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()  # Retorno com sucesso
        if response.status_code == 401:
            logout()  # Logout automático em caso de token inválido
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
```

## Gerenciamento de Sessão

A aplicação faz uso extensivo da sessão do Streamlit para manter estados entre requisições:

```python
if 'token' not in st.session_state:  # Verificação de token
    show_login()
```

As chaves de sessão devem ser strings descritivas e consistentes em todos os módulos:

- `'token'`: Armazena o token de autenticação JWT
- Outras chaves podem ser usadas para manter estados específicos da aplicação

## Tratamento de Erros

A aplicação utiliza tratamento de erros específico para respostas HTTP:

- **Status 200**: Requisição GET bem sucedida
- **Status 201**: Requisição POST bem sucedida (criação de recurso)
- **Status 401**: Token expirado ou inválido → chamada à função `logout()`
- Outros códigos de erro: Lançamento de exceptions com mensagem apropriada

```python
if response.status_code == 401:
    logout()  # Limpa a sessão e redireciona para login
    return None
raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
```

## Boas Práticas Observadas

1. **Separação de Responsabilidades**: Cada camada (page, service, repository) tem funções bem definidas
2. **Encapsulamento**: Uso de atributos privados com prefixo `__` e métodos bem definidos
3. **Retorno Consistente**: Funções retornam valores consistentes para tratamento uniforme
4. **Mensagens Claras**: Uso de mensagens de sucesso e erro específicas para o usuário
5. **Normalização de Dados**: Uso de `pd.json_normalize()` para padronizar dados antes de exibição em AgGrid
6. **Tratamento de Casos Vazios**: Verificação de dados nulos/vazios antes da exibição
7. **Validação de Formulários**: Inputs com validação apropriada (data limits, etc.)
8. **Verificação de Nomenclatura**: Cuidado com nomes de variáveis semelhantes para evitar erros de digitação (ex: `__genres_url` vs `__genress_url`)

## Erros Comuns a Evitar

- Erros de digitação em nomes de variáveis (typos), especialmente em URLs de API
- Uso inconsistente de nomes de variáveis entre diferentes métodos
- Esquecer de atualizar URLs ou endpoints quando mudam na API externa
- Não testar adequadamente o fluxo de autenticação e tratamento de tokens