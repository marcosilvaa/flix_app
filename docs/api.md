# Modulo de API

O modulo de API fornece o servico de autenticacao JWT para a aplicacao Flix App, abstraindo a comunicacao com o endpoint de autenticacao da API externa.

## Visao Geral

## API Externa

O modulo de API se comunica com a [Flix_API](https://github.com/marcosilvaa/flix_api), rodando localmente em `http://localhost:8000/api/v1/`. Esta API fornece os endpoints de autenticacao e dados que alimentam toda a aplicacao.

O modulo de API gerencia:
- Comunicacao com o servico de autenticacao externo
- Obtencao de tokens JWT via credenciais de usuario
- Tratamento de respostas e erros da API de autenticacao

## Estrutura do Modulo

```
api/
├── __init__.py
└── service.py       # Classe Auth para autenticacao JWT
```

O modulo de API e o unico que nao segue o padrao de tres camadas (page/service/repository). Possui apenas `service.py` com a classe `Auth`, sem pagina de interface ou repositorio.

## Componentes

### service.py

- **Classe**: `Auth`
- **Responsabilidade**: Gerenciar comunicacao com a API de autenticacao externa

#### `__init__()`

Configura as URLs para comunicacao:

```python
self.__base_url = 'http://localhost:8000/api/v1/'
self.__auth_url = f'{self.__base_url}authentication/token/'
```

#### `get_token(username, password)`

Realiza a autenticacao com a API:

1. Monta o payload: `{'username': username, 'password': password}`
2. Envia `requests.post(self.__auth_url, data=auth_payload)`
3. Se status code 200: retorna `response.json()` (contem chave `access` com o token JWT)
4. Caso contrario: retorna `{"error": "Erro ao autenticar. Status code: {status_code}"}`

**Nota**: Este metodo envia as credenciais como `data` (form-encoded), nao como JSON. O endpoint espera um POST com `Content-Type: application/x-www-form-urlencoded`.

## Integracao com Outros Modulos

### Modulo de Login

- `login.service.login()` importa `Auth` de `api.service`
- Cria uma instancia de `Auth` e chama `get_token(username, password)`
- Verifica se a resposta contem a chave `error` para determinar sucesso ou falha

### Modulos de Repositorio

- Os modulos de repositorio (genres, actors, movies, reviews) nao importam `Auth` diretamente
- Eles acessam o token armazenado em `st.session_state.token` apos o login
- O token e incluido como `Authorization: Bearer {token}` nos headers de todas as requisicoes

## Fluxo de Autenticacao

1. `login/page.py` coleta credenciais do usuario
2. `login/service.login()` chama `Auth.get_token()`
3. `Auth` faz POST para `/authentication/token/` na [Flix_API](https://github.com/marcosilvaa/flix_api)
4. Em caso de sucesso, o response contem `{"access": "<jwt_token>"}`
5. `login()` armazena o token em `st.session_state['token']`
6. Os repositorios leem o token de `st.session_state.token` para autenticar requisicoes
7. Se qualquer repositorio receber status 401, chama `logout()` que limpa toda a sessao