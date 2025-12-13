# Padrões de Código

Esta seção descreve as diretrizes de estilo e boas práticas adotadas no projeto Flix App.

## Estilo de Código

### Convenções de Nomenclatura

- **Variáveis e funções**: `snake_case` (ex: `get_user_info`, `movie_title`)
- **Classes**: `PascalCase` (ex: `GenreService`, `MovieRepository`)
- **Constantes**: `UPPER_SNAKE_CASE` (ex: `BASE_URL`, `MAX_RETRIES`)

### Importações

As importações seguem a ordem recomendada:

1. Bibliotecas padrão do Python
2. Bibliotecas de terceiros
3. Módulos do projeto

```python
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService
```

## Estrutura de Funções e Classes

### Funções

Funções devem ter nomes descritivos e seguir o padrão:

```python
def show_genres():  # Funções de página iniciam com "show_"
    st.write("Lista de Gêneros")
    # código aqui
```

### Classes

Classes seguem a convenção de ter um método `__init__` com inicialização de atributos privados usando prefixo `__`:

```python
class GenreRepository:
    def __init__(self):
        self.__base_url = 'https://marcosilva.pythonanywhere.com/api/v1/'
```

## Gerenciamento de Sessão

A aplicação faz uso extensivo da sessão do Streamlit para manter estados entre requisições:

```python
if 'token' not in st.session_state:  # Verificação de token
    show_login()
```

As chaves de sessão devem ser strings descritivas e consistentes em todos os módulos.

## Tratamento de Erros

A aplicação utiliza tratamento de erros específico para respostas HTTP:

```python
if response.status_code == 401:
    logout()
    return None
raise Exception(f'Erro ao obter dados da API. Status Cod: {response.status_code}')
```

## Boas Práticas Observadas

1. **Separação de Responsabilidades**: Cada arquivo tem uma função bem definida
2. **Encapsulamento**: Uso de atributos privados com prefixo `__`
3. **Retorno Consistente**: Funções retornam valores consistentes para tratamento uniforme
4. **Mensagens Claras**: Uso de mensagens de sucesso e erro específicas para o usuário
5. **Normalização de Dados**: Uso de `pd.json_normalize()` para padronizar dados antes de exibição