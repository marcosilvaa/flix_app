# Módulo de Atores

O módulo de atores é responsável pelo cadastro e listagem de atores na aplicação Flix App, permitindo o gerenciamento de informações de elenco para associação com os filmes.

## Visão Geral

O módulo de atores gerencia:
- Listagem de atores cadastrados com informações detalhadas
- Cadastro de novos atores com nome, data de nascimento e nacionalidade
- Integração com o módulo de filmes para associação de elenco
- Exibição de dados em formato tabular com AgGrid

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
actors/
├── __init__.py
├── page.py        # Interface de usuário para atores
├── service.py     # Lógica de negócio para atores
└── repository.py  # Camada de acesso a dados para atores
```

## Componentes

### page.py
- **Função**: `show_actors()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de atores
- **Características**:
  - Exibe lista de atores em formato tabular com AgGrid
  - Formulário para cadastro de novos atores com campos:
    - Nome do ator
    - Data de nascimento (com validação de range)
    - Nacionalidade (dropdown com opções fixas)
  - Tratamento de casos vazios com mensagem de aviso
  - Feedback para o usuário após operações de cadastro

### service.py
- **Classe**: `ActorService`
- **Responsabilidade**: Implementar a lógica de negócios para atores
- **Características**:
  - Método `get_actors()`: Obtém a lista de atores da API
  - Método `create_actor()`: Prepara e envia dados para cadastro de ator
  - Integração com o repositório para comunicação com a API
  - Preparação de dados antes de enviar à camada de repositório

### repository.py
- **Classe**: `ActorRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operações de atores
- **Características**:
  - URL base e headers configurados com token de autenticação
  - Métodos para obtenção e criação de atores na API
  - Tratamento de respostas HTTP (200, 201, 401)
  - Encapsulamento de detalhes de comunicação com a API
  - Chamada à função `logout()` em caso de falha de autenticação (401)

## Funcionalidades

### Listagem de Atores
- Exibe atores em formato tabular interativo com AgGrid
- Suporte para ordenação, filtragem e redimensionamento de colunas
- Tratamento de caso vazio com mensagem amigável ao usuário
- Atualização automática após operações de criação

### Cadastro de Atores
- Formulário com validações de dados (datas, campos obrigatórios)
- Validação de data de nascimento (intervalo de 1900 até data atual)
- Opções de nacionalidade pré-definidas (BRAZIL, USA)
- Feedback visual de sucesso ou erro após tentativa de cadastro

## Integrações

### Com Módulo de Filmes
- Importação de `ActorService` para obtenção da lista de atores
- Criação de mapeamento nome:id para seleção no formulário de filme
- Associação de atores ao elenco de filmes

## Componentes de UI

- **AgGrid**: Componente para exibição tabular interativa de atores
- **Campos de Texto**: Nome do ator
- **Date Input**: Data de nascimento com validação de range
- **Dropdown**: Nacionalidade com opções pré-definidas
- **Botões**: Cadastro de novo ator
- **Mensagens**: Feedback de sucesso ou erro para o usuário

## Padrões de Código

- Função de página segue padrão `show_nome_modulo`
- Serviço implementa injeção de dependência do repositório
- Repositório encapsula URLs e headers de autenticação
- Tratamento consistente de erros HTTP
- Normalização de dados com `pd.json_normalize()` para exibição