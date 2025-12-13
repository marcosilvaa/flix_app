# Módulo de Avaliações

O módulo de avaliações é responsável pela exibição e cadastro de avaliações de filmes na aplicação Flix App. Atualmente, este módulo encontra-se em fase inicial de desenvolvimento com implementação parcial.

## Visão Geral

O módulo de avaliações gerencia:
- Listagem de avaliações cadastradas
- Interface para cadastro de novas avaliações
- Exibição de dados em formato tabular com AgGrid
- **Status**: Implementação parcial, não integrado com a API externa

## Estrutura do Módulo

O módulo está organizado da seguinte forma:

```
reviews/
├── __init__.py
└── page.py        # Interface de usuário para avaliações (implementação parcial)
```

## Componentes

### page.py
- **Função**: `show_reviews()`
- **Responsabilidade**: Exibir a interface de listagem e cadastro de avaliações
- **Características**:
  - Exibe lista de avaliações em formato tabular com AgGrid (dados estáticos por enquanto)
  - Formulário para cadastro de novas avaliações (funcionalidade limitada)
  - Implementação parcial - dados não são persistidos nem integrados com a API
  - Exemplo com dados mockados para demonstração

## Funcionalidades Atuais

### Listagem de Avaliações
- Exibe avaliações em formato tabular interativo com AgGrid
- Utiliza dados mockados definidos como variável `reviews` no início do arquivo
- Coluna de identificação e estrelas como exemplo de estrutura

### Cadastro de Avaliações
- Formulário com campo para "nota da avaliação"
- Funcionalidade limitada sem persistência de dados
- Feedback visual de sucesso após tentativa de cadastro

## Limitações Atuais

### Implementação Incompleta
- Módulo não está integrado com a API externa
- Dados são armazenados localmente como variáveis estáticas
- Não há persistência real de avaliações
- Funcionalidades de edição ou exclusão não estão implementadas
- Não há relacionamento com os módulos de filmes ou usuários
- Estrutura de dados de avaliações é simplificada e provisória

### Arquitetura Incompleta
- Ausência de camadas de serviço e repositório
- Não segue o padrão de arquitetura em camadas dos outros módulos
- Não utiliza token de autenticação para operações
- Não implementa validações completas

## Componentes de UI

- **AgGrid**: Componente para exibição tabular interativa de avaliações
- **Campos de Texto**: Nota da avaliação
- **Botões**: Cadastro de nova review
- **Mensagens**: Feedback de sucesso para o usuário

## Futuras Implementações

Para completar o módulo de avaliações, seriam necessárias as seguintes implementações:
- Camadas de serviço e repositório seguindo o padrão da aplicação
- Integração com a API externa para persistência de dados
- Relacionamento com entidades de filmes e usuários
- Sistema de estrelas ou esquema de classificação mais completo
- Validações de negócio adequadas
- Funcionalidades de edição e exclusão de avaliações

## Padrões de Código

A implementação atual não segue completamente os padrões da aplicação, pois:
- Não implementa o padrão de arquitetura em camadas
- Não utiliza serviço e repositório para persistência
- Utiliza dados mockados em vez de dados reais da API