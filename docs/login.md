# Módulo de Login

O módulo de login é responsável pela autenticação de usuários na aplicação Flix App, implementando um sistema de autenticação baseado em JWT (JSON Web Tokens).

## Visão Geral

O módulo de login gerencia:
- Interface de login para entrada de credenciais de usuário
- Autenticação com a API externa via JWT
- Armazenamento seguro do token na sessão do Streamlit
- Gerenciamento de logout e limpeza de sessão

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
login/
├── __init__.py
├── page.py      # Interface de usuário para login
└── service.py   # Lógica de autenticação e sessão
```

## Componentes

### page.py
- **Função**: `show_login()`
- **Responsabilidade**: Exibir a interface de login com campos para usuário e senha
- **Características**:
  - Formulário com campos de texto para usuário e senha (oculta)
  - Botão de login que aciona o processo de autenticação
  - Exibição de erros de autenticação

### service.py
- **Funções**: `login()` e `logout()`
- **Responsabilidade**: Gerenciar o processo de autenticação e sessão
- **Características**:
  - Função `login()`: Chama o serviço de autenticação para obter token JWT
  - Armazenamento do token em `st.session_state.token`
  - Função `logout()`: Limpa todos os dados da sessão e redireciona para login
  - Tratamento de erros de autenticação

### api/service.py
- **Classe**: `Auth`
- **Responsabilidade**: Comunicação com a API de autenticação externa
- **Características**:
  - Realiza requisição POST para `/authentication/token/`
  - Retorna token JWT em caso de credenciais válidas
  - Tratamento de erros de autenticação

## Fluxo de Autenticação

1. **Acesso à Aplicação**: Sistema verifica existência de token na sessão
2. **Sem Token**: Usuário é redirecionado para a tela de login
3. **Formulário de Login**: Usuário insere credenciais (usuário/senha)
4. **Processo de Autenticação**: 
   - Função `login()` é chamada
   - Serviço `Auth.get_token()` realiza chamada à API externa
   - Em caso de sucesso, token é armazenado em `st.session_state.token`
5. **Autenticação Bem-Sucedida**: Aplicação é reiniciada e usuário acessa o conteúdo protegido
6. **Logout**: Ao fazer logout, toda a sessão é limpa (`st.session_state`)

## Componentes de UI

- **Campos de Entrada**: Usuário e senha (senha oculta)
- **Botão de Login**: Aciona o processo de autenticação
- **Mensagens**: Exibição de erros de autenticação, se necessário

## Segurança

- Tokens JWT armazenados temporariamente na sessão do Streamlit
- Em caso de falha de autenticação (401), sessão é automaticamente limpa
- Sistema de logout remove completamente todos os dados da sessão
- Credenciais não são armazenadas no cliente

## Padrões de Código

- Funções de autenticação seguem convenções de tratamento de erros
- Armazenamento de token utiliza chave `token` no `st.session_state`
- Função `logout()` itera sobre todas as chaves do estado para garantir limpeza completa