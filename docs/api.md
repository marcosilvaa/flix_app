# Módulo de API

O módulo de API é responsável pela comunicação com o serviço externo de autenticação JWT na aplicação Flix App, fornecendo serviços de autenticação para o módulo de login.

## Visão Geral

O módulo de API gerencia:
- Comunicação com o serviço de autenticação externo
- Obtenção de tokens JWT para autenticação
- Tratamento de respostas e erros da API de autenticação
- Abstração dos detalhes de comunicação HTTP para autenticação

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
api/
├── __init__.py
└── service.py       # Serviço de autenticação JWT
```

## Componentes

### service.py
- **Classe**: `Auth`
- **Responsabilidade**: Gerenciar comunicação com a API de autenticação externa
- **Características**:
  - URL base configurada para o serviço de autenticação
  - Método `get_token()` para obtenção de token JWT via credenciais
  - Tratamento de respostas HTTP e erros de autenticação
  - Retorno de JSON com token de acesso ou mensagem de erro

#### Classe Auth
- **Método `__init__()`**: Configura URL base e endpoint de autenticação
  - `__base_url`: URL base da API externa
  - `__auth_url`: Endpoint específico para obtenção de token (`/authentication/token/`)
- **Método `get_token(username, password)`**: Realiza autenticação com a API
  - Recebe credenciais de usuário e senha
  - Envia requisição POST para o endpoint de autenticação
  - Retorna JSON com token em caso de sucesso
  - Retorna objeto de erro em caso de falha de autenticação

## Funcionalidades

### Obtenção de Token JWT
- Implementa comunicação com endpoint `/authentication/token/`
- Envia credenciais via payload POST
- Tratamento de resposta HTTP 200 (sucesso)
- Tratamento de erros com retorno de mensagem descritiva
- Formato de retorno: JSON com token de acesso ou objeto de erro

## Integrações

### Com Módulo de Login
- Importado por `login.service` para obtenção de tokens
- Utilizado na função `login()` para autenticação do usuário
- Fornece tokens necessários para acesso à API protegida

## Padrões de Código

- Classe `Auth` implementa padrão de serviço com responsabilidade única
- Atributos privados com prefixo `__` para encapsulamento
- Tratamento consistente de erros HTTP
- Retorno padronizado para sucesso e erro