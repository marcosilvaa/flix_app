# Modulo de Login

O modulo de login e responsavel pela autenticacao de usuarios na aplicacao Flix App, implementando um sistema baseado em JWT (JSON Web Tokens).

## Visao Geral

O modulo de login gerencia:
- Interface de login para entrada de credenciais (usuario e senha)
- Autenticacao com a API externa via JWT
- Armazenamento do token na sessao do Streamlit (`st.session_state.token`)
- Gerenciamento de logout com limpeza completa da sessao

## Estrutura do Modulo

```
login/
├── __init__.py
└── page.py       # Interface de login (show_login)
└── service.py     # Funcoes login() e logout()
```

O modulo de login usa funcoes (nao classes) para a camada de servico, diferente dos outros modulos que usam classes Service.

## Componentes

### page.py

- **Funcao**: `show_login()`
- **Responsabilidade**: Exibir a interface de login com campos para usuario e senha
- **Caracteristicas**:
  - Campo `st.text_input` para usuario
  - Campo `st.text_input` com `type='password'` para senha (oculta)
  - Botao "Login" que aciona a funcao `login(username, password)`
  - Mensagens de erro sao gerenciadas pela funcao `login()` do service

### service.py

- **Funcoes**: `login()` e `logout()`
- **`login(username, password)`**:
  1. Cria instancia de `Auth` do modulo `api.service`
  2. Chama `auth_service.get_token(username, password)`
  3. Se a resposta contem a chave `error`, exibe `st.error()` com a mensagem
  4. Se bem-sucedido, armazena o token em `st.session_state.token` e chama `st.rerun()`
- **`logout()`**:
  1. Itera sobre todas as chaves de `st.session_state` e as remove
  2. Chama `st.rerun()` para redirecionar para a tela de login

### api/service.py (Classe Auth)

- **Classe**: `Auth`
- **Responsabilidade**: Comunicacao com a API de autenticacao externa
- **`__init__()`**:
  - `self.__base_url = 'http://localhost:8000/api/v1/'`
  - `self.__auth_url = f'{self.__base_url}authentication/token/'`
- **`get_token(username, password)`**:
  - Envia POST com `data={'username': username, 'password': password}`
  - Retorna `response.json()` em caso de status 200 (contem chave `access` com o token JWT)
  - Retorna `{"error": "Erro ao autenticar. Status code: ..."}` em caso de falha

## Fluxo de Autenticacao

```
app.py verifica st.session_state.token
├── Token ausente → show_login()
│   ├── Usuario preenche credenciais
│   ├── click "Login" → login(username, password)
│   │   ├── Auth.get_token(username, password)
│   │   │   └── POST /authentication/token/ → response
│   │   ├── Sucesso: st.session_state.token = response['access'] → st.rerun()
│   │   └── Falha: st.error(mensagem de erro)
│   └── Pagina recarregada com token → acesso ao menu lateral
└── Token presente → exibe menu lateral com opcoes
```

## Seguranca

- Tokens JWT armazenados temporariamente em `st.session_state`
- Credenciais nao sao persistidas — apenas enviadas na requisicao de autenticacao
- Em caso de resposta 401 de qualquer endpoint, `logout()` e chamado automaticamente
- `logout()` remove todas as chaves de `st.session_state`, incluindo o token e caches de dados