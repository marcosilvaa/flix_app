import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.services import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()
    if movies:
        st.write("Lista de Filmes")
        movies_df = pd.json_normalize(movies)
        movies_df.drop(columns=['actors'])
        AgGrid(
            data=movies_df,
            key='movies_grid',
            reload=True
        )
    else:
        st.warning('Nenhum Filme encontrado!')

    st.title("Cadastrar novo Filme")

    title = st.text_input('Nome do Filme')

    genres_service = GenreService()
    genres = genres_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
        label='Gênero',
        options=list(genre_names.keys()),
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect("Atores/Atrizes", list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            release_date=release_date,
            resume=resume,
        )
        if new_movie:
            st.success(f"Filme '{title}' cadastrado com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao cadastrar o filme. Verifique os campos!")
