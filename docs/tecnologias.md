# Tecnologias Utilizadas

Este documento lista as tecnologias, frameworks e bibliotecas utilizadas no projeto Flix App.

## Dependências do Projeto

As dependências estão especificadas no arquivo `pyproject.toml`:

- **Python**: >=3.14
- **Streamlit**: >=1.52.1 (Framework para interface gráfica)
- **requests**: >=2.32.5 (Para chamadas HTTP à API externa)
- **streamlit-aggrid**: >=1.2.1 (Para componentes de grade de dados)
- **pandas**: Manipulação e normalização de dados

## Frameworks e Bibliotecas

### Streamlit
- Framework utilizado para criar a interface web
- Permite desenvolvimento rápido de aplicações web com Python
- Utiliza sessões para manter estado entre interações
- Oferece diversos componentes de UI (inputs, botões, tabelas, etc.)

### Pandas
- Usado para manipulação e normalização de dados
- Facilita a conversão de dados para formato adequado para exibição em tabelas
- Função `json_normalize()` usada para converter JSONs complexos em DataFrames
- Integração com Streamlit-AgGrid para exibição de dados

### Requests
- Biblioteca para realização de requisições HTTP
- Utilizada para comunicação com a API externa
- Tratamento de cabeçalhos e autenticação JWT
- Manipulação de diferentes códigos de resposta HTTP

### Streamlit-AgGrid
- Componente para exibição de dados em formato de tabela interativa
- Integração com Streamlit
- Suporte para recarregamento de dados, ordenação, filtragem e redimensionamento de colunas
- Baseado na biblioteca Ag-Grid JavaScript

### Datetime
- Biblioteca padrão Python para manipulação de datas
- Utilizada para inputs de data com validação de range (ex: datas de nascimento)

## Infraestrutura

### API Externa
- Localização: https://marcosilva.pythonanywhere.com/api/v1/
- Protocolo: REST API
- Autenticação: JWT (JSON Web Tokens)
- Endpoints: authentication/token/, genres/, actors/, movies/, etc.
- Formato de dados: JSON

## Gerenciamento de Pacotes

O projeto utiliza o sistema moderno de gerenciamento de pacotes Python:

- **pyproject.toml**: Configuração do projeto e dependências
- **uv.lock**: Lock file para garantir consistência nas dependências
- **uv**: Gerenciador de pacotes Python (moderno e rápido)

## Patamares de Segurança

### Autenticação JWT
- Tokens armazenados na sessão do Streamlit
- Validação automática em cada chamada à API
- Redirecionamento automático para login em caso de token inválido
- Sistema de logout que limpa toda a sessão