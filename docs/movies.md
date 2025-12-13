# Módulo de Filmes

O módulo de filmes é responsável pelo cadastro e listagem de filmes na aplicação Flix App, integrando informações de gêneros e atores para criar uma experiência completa de gerenciamento de filmes.

## Visão Geral

O módulo de filmes gerencia:
- Listagem de filmes cadastrados com informações detalhadas
- Cadastro de novos filmes com associação a gêneros e atores
- Integração com módulos de gêneros e atores para associação de entidades
- Exibição de dados em formato tabular com AgGrid

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
movies/
├── __init__.py
├── page.py        # Interface de usuário para filmes
├── repository.py  # Camada de acesso a dados para filmes
└── services.py    # Lógica de negócio para filmes
```

## Componentes

### page.py
- **Função**: `show_movies()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de filmes
- **Características**:
  - Exibe lista de filmes em formato tabular com AgGrid
  - Formulário para cadastro de novos filmes com campos:
    - Título do filme
    - Seleção de gênero (dropdown com gêneros da API)
    - Seleção múltipla de atores (multiselect com atores da API)
    - Data de lançamento (com validação de range)
    - Resumo do filme
  - Tratamento de casos vazios com mensagem de aviso
  - Feedback para o usuário após operações de cadastro

### services.py
- **Classe**: `MovieService`
- **Responsabilidade**: Implementar a lógica de negócios para filmes
- **Características**:
  - Método `get_movies()`: Obtém a lista de filmes da API
  - Método `create_movie()`: Prepara e envia dados para cadastro de filme
  - Integração com o repositório para comunicação com a API
  - Preparação de dados antes de enviar à camada de repositório

### repository.py
- **Classe**: `MovieRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operações de filmes
- **Características**:
  - URL base e headers configurados com token de autenticação
  - Métodos para obtenção e criação de filmes na API
  - Tratamento de respostas HTTP (200, 201, 401)
  - Encapsulamento de detalhes de comunicação com a API
  - Chamada à função `logout()` em caso de falha de autenticação (401)

## Funcionalidades

### Listagem de Filmes
- Exibe filmes em formato tabular interativo com AgGrid
- Suporte para ordenação, filtragem e redimensionamento de colunas
- Tratamento de caso vazio com mensagem amigável ao usuário
- Atualização automática após operações de criação

### Cadastro de Filmes
- Formulário com validações de dados (datas, campos obrigatórios)
- Seleção de gênero entre opções disponíveis da API
- Seleção múltipla de atores para elenco do filme
- Validação de data de lançamento (intervalo de 1800 até data atual)
- Feedback visual de sucesso ou erro após tentativa de cadastro

## Integrações

### Com Módulo de Gêneros
- Importação de `GenreService` para obtenção da lista de gêneros
- Criação de mapeamento nome:id para seleção no formulário de filme
- Associação do ID do gênero selecionado ao novo filme

### Com Módulo de Atores
- Importação de `ActorService` para obtenção da lista de atores
- Criação de mapeamento nome:id para seleção no formulário de filme
- Suporte para associação múltipla de atores ao novo filme

## Componentes de UI

- **AgGrid**: Componente para exibição tabular interativa de filmes
- **Campos de Texto**: Título e resumo do filme
- **Dropdown**: Seleção de gênero
- **Multiselect**: Seleção múltipla de atores
- **Date Input**: Data de lançamento com validação de range
- **Botões**: Cadastro de novo filme
- **Mensagens**: Feedback de sucesso ou erro para o usuário

## Padrões de Código

- Função de página segue padrão `show_nome_modulo`
- Serviço implementa injeção de dependência do repositório
- Repositório encapsula URLs e headers de autenticação
- Tratamento consistente de erros HTTP
- Normalização de dados com `pd.json_normalize()` para exibição