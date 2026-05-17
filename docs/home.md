# Modulo Home

O modulo home e responsavel pelo dashboard de estatisticas da aplicacao Flix App, exibindo informacoes consolidadas sobre filmes e avaliacoes. Os dados sao fornecidos pela [Flix_API](https://github.com/marcosilvaa/flix_api) atraves do endpoint `/movies/stats/`.

## Visao Geral

O modulo home exibe:
- Grafico de pizza com distribuicao de filmes por genero (Plotly)
- Total de filmes cadastrados
- Quantidade de filmes por genero
- Total de avaliacoes cadastradas
- Media geral de estrelas nas avaliacoes

## Estrutura do Modulo

```
home/
├── __init__.py
└── page.py        # Interface do dashboard de estatisticas
```

O modulo home nao possui camadas de `service.py` e `repository.py`. Em vez disso, importa `MovieService` diretamente de `movies.services` para obter as estatisticas.

## Componentes

### page.py

- **Funcao**: `show_home()`
- **Responsabilidade**: Exibir o dashboard de estatisticas de filmes
- **Dependencias**: `movies.services.MovieService`, `plotly.express`
- **Caracteristicas**:
  - Instancia `MovieService` e chama `get_movie_stats()`
  - Se houver dados de filmes por genero, renderiza grafico de pizza com `px.pie()`
  - Exibe total de filmes, total de avaliacoes e media de estrelas em texto
  - Lista cada genero com sua contagem de filmes

## Integracao com MovieService

O modulo home depende de `MovieService.get_movie_stats()`, que por sua vez chama `MovieRepository.get_movie_stats()`. Este metodo faz GET para o endpoint `/movies/stats/` da API, que retorna:

```json
{
  "movies_by_genre": [
    {"genre__name": "Acao", "count": 5},
    {"genre__name": "Comedia", "count": 3}
  ],
  "total_movies": 8,
  "total_reviews": 12,
  "average_stars": 4.2
}
```

## Componentes de UI

- **`st.plotly_chart()`**: Renderiza o grafico de pizza do Plotly
- **`st.title()`**: Titulo "Estatisticas de Filmes"
- **`st.subheader()`** e **`st.write()`**: Exibicao dos contadores e listas

## Observacoes

- O modulo nao segue o padrao de tres camadas (page/service/repository) dos demais modulos
- Se a lista de `movies_by_genre` estiver vazia, o grafico de pizza nao e renderizado
- Os contadores de total e media sao sempre exibidos, mesmo que os dados sejam zero