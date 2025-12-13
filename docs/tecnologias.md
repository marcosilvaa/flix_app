# Tecnologias Utilizadas

Este documento lista as tecnologias, frameworks e bibliotecas utilizadas no projeto Flix App.

## Dependências do Projeto

As dependências estão especificadas no arquivo `pyproject.toml`:

- **Python**: >=3.14
- **Streamlit**: >=1.52.1 (Framework para interface gráfica)
- **requests**: >=2.32.5 (Para chamadas HTTP à API externa)
- **streamlit-aggrid**: >=1.2.1 (Para componentes de grade de dados)

## Frameworks e Bibliotecas

### Streamlit
- Framework utilizado para criar a interface web
- Permite desenvolvimento rápido de aplicações web com Python
- Utiliza sessões para manter estado entre interações

### Pandas
- Usado para manipulação e normalização de dados
- Facilita a conversão de dados para formato adequado para exibição em tabelas

### Requests
- Biblioteca para realização de requisições HTTP
- Utilizada para comunicação com a API externa
- Tratamento de cabeçalhos e autenticação

### Streamlit-AgGrid
- Componente para exibição de dados em formato de tabela interativa
- Integração com Streamlit
- Suporte para recarregamento de dados

## Infraestrutura

### API Externa
- Localização: https://marcosilva.pythonanywhere.com/api/v1/
- Protocolo: REST API
- Autenticação: JWT (JSON Web Tokens)
- Endpoints: authentication/token/, genres/, etc.

## Gerenciamento de Pacotes

O projeto utiliza o sistema moderno de gerenciamento de pacotes Python:

- **pyproject.toml**: Configuração do projeto e dependências
- **uv.lock**: Lock file para garantir consistência nas dependências