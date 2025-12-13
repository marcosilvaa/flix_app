# Arquitetura da Aplicação

Este documento descreve o padrão arquitetural utilizado no projeto Flix App.

## Visão Geral

O Flix App segue um padrão de arquitetura baseado em camadas (Layered Architecture) com separação clara de responsabilidades. Cada módulo funcional é organizado em três camadas principais:

1. **Camada de Apresentação (Page)**
2. **Camada de Serviço (Service)**
3. **Camada de Repositório (Repository)**

## Padrões de Arquitetura

### 1. Camada de Apresentação (Page)

Localizada nos arquivos `page.py` de cada módulo, esta camada é responsável por:

- Exibir interfaces de usuário usando Streamlit
- Integrar componentes como AgGrid para exibição de tabelas
- Coletar entradas do usuário
- Acionar funções das camadas inferiores

Exemplo:
```python
def show_actors():
    st.write("Lista de Atores")
    # Chamadas para a camada de serviço
```

### 2. Camada de Serviço (Service)

Localizada nos arquivos `service.py` de cada módulo, esta camada é responsável por:

- Implementar a lógica de negócios específica do domínio
- Orquestrar chamadas entre diferentes repositórios
- Validar regras de negócio

Exemplo:
```python
class GenreService:
    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        return self.genre_repository.get_genres()
```

### 3. Camada de Repositório (Repository)

Localizada nos arquivos `repository.py` de cada módulo, esta camada é responsável por:

- Comunicar-se com a API externa
- Gerenciar autenticação e autorização (tokens)
- Tratar respostas HTTP e possíveis erros

Exemplo:
```python
class GenreRepository:
    def __init__(self):
        self.__base_url = 'https://marcosilva.pythonanywhere.com/api/v1/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        # Chamada à API externa
```

## Fluxo de Autenticação

A aplicação utiliza um sistema de autenticação baseado em token JWT:

1. Na inicialização, verifica-se se existe um token na sessão (`st.session_state`)
2. Se não houver, o usuário é redirecionado para a tela de login
3. Após o login bem-sucedido, o token é armazenado na sessão
4. Os tokens são usados nas chamadas às APIs protegidas
5. Em caso de falha de autenticação (401), a sessão é limpa automaticamente

## Componentes de UI

A aplicação utiliza os seguintes componentes de interface:

- **Streamlit**: Framework principal para construção da interface
- **st_aggrid**: Componente para exibição de tabelas interativas
- **Componentes nativos do Streamlit**: inputs, botões, divisores, etc.