# Módulo de Gêneros

O módulo de gêneros é responsável pelo cadastro e listagem de gêneros na aplicação Flix App, permitindo a categorização de filmes por diferentes tipos e estilos.

## Visão Geral

O módulo de gêneros gerencia:
- Listagem de gêneros cadastrados
- Cadastro de novos gêneros com nome descritivo
- Integração com o módulo de filmes para categorização
- Exibição de dados em formato tabular com AgGrid

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
genres/
├── __init__.py
├── page.py        # Interface de usuário para gêneros
├── service.py     # Lógica de negócio para gêneros
└── repository.py  # Camada de acesso a dados para gêneros
```

## Componentes

### page.py
- **Função**: `show_genres()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de gêneros
- **Características**:
  - Exibe lista de gêneros em formato tabular com AgGrid
  - Formulário para cadastro de novo gênero com campo de nome
  - Tratamento de casos vazios com mensagem de aviso
  - Feedback para o usuário após operações de cadastro

### service.py
- **Classe**: `GenreService`
- **Responsabilidade**: Implementar a lógica de negócios para gêneros
- **Características**:
  - Método `get_genres()`: Obtém a lista de gêneros da API
  - Método `create_genre()`: Prepara e envia dados para cadastro de gênero
  - Integração com o repositório para comunicação com a API
  - Preparação de dados antes de enviar à camada de repositório

### repository.py
- **Classe**: `GenreRepository`
- **Responsabilidade**: Comunicar-se com a API externa para operações de gêneros
- **Características**:
  - URL base e headers configurados com token de autenticação
  - Métodos para obtenção e criação de gêneros na API
  - Tratamento de respostas HTTP (200, 201, 401)
  - Encapsulamento de detalhes de comunicação com a API
  - Chamada à função `logout()` em caso de falha de autenticação (401)

## Funcionalidades

### Listagem de Gêneros
- Exibe gêneros em formato tabular interativo com AgGrid
- Suporte para ordenação, filtragem e redimensionamento de colunas
- Tratamento de caso vazio com mensagem amigável ao usuário
- Atualização automática após operações de criação

### Cadastro de Gêneros
- Formulário com campo para nome do gênero
- Validação de campos obrigatórios
- Feedback visual de sucesso ou erro após tentativa de cadastro

## Integrações

### Com Módulo de Filmes
- Importação de `GenreService` para obtenção da lista de gêneros
- Criação de mapeamento nome:id para seleção no formulário de filme
- Associação do gênero ao filme

## Componentes de UI

- **AgGrid**: Componente para exibição tabular interativa de gêneros
- **Campos de Texto**: Nome do gênero
- **Botões**: Cadastro de novo gênero
- **Mensagens**: Feedback de sucesso ou erro para o usuário

## Padrões de Código

- Função de página segue padrão `show_nome_modulo`
- Serviço implementa injeção de dependência do repositório
- Repositório encapsula URLs e headers de autenticação
- Tratamento consistente de erros HTTP
- Normalização de dados com `pd.json_normalize()` para exibição