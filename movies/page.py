import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, AgGridTheme
from movies.services import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.subheader('Filmes Cadastrados')
        movies_df = pd.json_normalize(movies)
        cols_to_drop = [c for c in ['actors'] if c in movies_df.columns]
        if cols_to_drop:
            movies_df = movies_df.drop(columns=cols_to_drop)
        AgGrid(
            movies_df,
            theme=AgGridTheme.STREAMLIT,
            key='movies_grid',
            reload_data=True,
        )
    else:
        st.warning('Nenhum Filme encontrado!')

    st.divider()

    with st.expander('Cadastrar novo Filme', expanded=not movies):
        title = st.text_input('Nome do Filme', key='movie_title_input')

        col1, col2 = st.columns(2)
        with col1:
            genres_service = GenreService()
            genres = genres_service.get_genres()
            genre_names = {genre['name']: genre['id'] for genre in genres} if genres else {}
            selected_genre_name = st.selectbox(
                label='Gênero',
                options=list(genre_names.keys()) if genre_names else ['—'],
                key='movie_genre_input',
            )

        with col2:
            release_date = st.date_input(
                label='Data de Lançamento',
                value=datetime.today(),
                min_value=datetime(1800, 1, 1).date(),
                max_value=datetime.today(),
                format='DD/MM/YYYY',
                key='movie_date_input',
            )

        actor_service = ActorService()
        actors = actor_service.get_actors()
        actor_names = {actor['name']: actor['id'] for actor in actors} if actors else {}
        selected_actors_names = st.multiselect(
            'Atores/Atrizes',
            list(actor_names.keys()) if actor_names else [],
            key='movie_actors_input',
        )
        selected_actors_ids = [actor_names[name] for name in selected_actors_names]

        resume = st.text_area('Resumo', key='movie_resume_input')

        if st.button('Cadastrar', key='movie_create_btn'):
            if not title:
                st.error('O campo nome não pode estar vazio.')
            elif not genre_names:
                st.error('Nenhum gênero disponível. Cadastre um gênero primeiro.')
            else:
                new_movie = movie_service.create_movie(
                    title=title,
                    genre=genre_names.get(selected_genre_name),
                    actors=selected_actors_ids,
                    release_date=release_date,
                    resume=resume,
                )
                if new_movie:
                    st.success(f"Filme '{title}' cadastrado com sucesso!")
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar o filme. Verifique os campos!')
