import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.services import MovieService


def show_reviews():
    revies_service = ReviewService()
    reviews = revies_service.get_reviews()

    if reviews:
        st.write("Lista de avaliações")

        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            key='movies_grid',
            reload=True
        )
    else:
        st.warning("Nenhuma avaliação encontrada")

    st.title("Cadastrar nova Review")

    movies_service = MovieService()
    movies = movies_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox("Filme", list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = revies_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.success(f"Review do filme '{selected_movie_title}' cadastrado com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao cadastrar avaliação. Verifique os campos!")
