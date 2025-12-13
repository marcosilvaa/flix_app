# Estrutura do Projeto

Esta seção descreve a organização dos arquivos e pastas do projeto Flix App.

## Visão Geral

```
flix-app/
├── app.py              # Arquivo principal da aplicação Streamlit
├── main.py             # Arquivo de execução alternativo
├── pyproject.toml      # Configurações do projeto e dependências
├── uv.lock            # Lock file para gerenciamento de pacotes
├── .gitignore         # Arquivos ignorados pelo Git
├── .python-version    # Versão do Python utilizada
├── actors/            # Módulo de atores
│   ├── __init__.py
│   ├── page.py        # Interface de usuário para atores
│   ├── repository.py  # Camada de acesso a dados para atores
│   └── service.py     # Lógica de negócio para atores
├── api/               # Módulo de serviços de API
│   ├── __init__.py
│   └── service.py     # Serviço de autenticação
├── genres/            # Módulo de gêneros (completo)
│   ├── __init__.py
│   ├── page.py        # Interface de usuário para gêneros
│   ├── repository.py  # Camada de acesso a dados para gêneros
│   └── service.py     # Lógica de negócio para gêneros
├── login/             # Módulo de autenticação
│   ├── __init__.py
│   ├── page.py        # Tela de login
│   └── service.py     # Funções de autenticação
├── movies/            # Módulo de filmes
│   ├── __init__.py
│   ├── page.py        # Interface de usuário para filmes
│   ├── repository.py  # Camada de acesso a dados para filmes
│   └── services.py    # Lógica de negócio para filmes
├── reviews/           # Módulo de avaliações
│   ├── __init__.py
│   └── page.py        # Interface de usuário para avaliações
└── docs/              # Pasta de documentação
    └── ...
```

## Descrição das Pastas

- **actors/**: Funcionalidade relacionada ao cadastro e listagem de atores (CRUD completo)
- **api/**: Serviços de comunicação com API externa (autenticação JWT)
- **genres/**: Funcionalidade completa de gêneros com integração à API (CRUD completo)
- **login/**: Sistema de autenticação e autorização (login/logout)
- **movies/**: Funcionalidade relacionada ao cadastro e listagem de filmes (CRUD incompleto)
- **reviews/**: Funcionalidade para avaliações de filmes (implementação parcial)
- **docs/**: Documentação do projeto