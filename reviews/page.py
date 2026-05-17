import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, AgGridTheme
from reviews.service import ReviewService
from movies.services import MovieService


def show_reviews():
    reviews_service = ReviewService()
    reviews = reviews_service.get_reviews()

    if reviews:
        st.subheader('Avaliações Cadastradas')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            reviews_df,
            theme=AgGridTheme.STREAMLIT,
            key='reviews_grid',
            reload_data=True,
        )
    else:
        st.warning('Nenhuma avaliação encontrada')

    st.divider()

    with st.expander('Cadastrar nova Avaliação', expanded=not reviews):
        movies_service = MovieService()
        movies = movies_service.get_movies()
        if not movies:
            st.info('Nenhum filme disponível. Cadastre um filme primeiro.')
            return

        movie_titles = {movie['title']: movie['id'] for movie in movies}
        selected_movie_title = st.selectbox(
            'Filme',
            list(movie_titles.keys()),
            key='review_movie_input',
        )

        col1, col2 = st.columns(2)
        with col1:
            stars = st.number_input(
                label='Estrelas',
                min_value=0,
                max_value=5,
                step=1,
                key='review_stars_input',
            )
        with col2:
            stars_display = '★' * int(stars) + '☆' * (5 - int(stars))
            st.markdown(
                f'<span style="font-size:2em; color:#FFD700;">{stars_display}</span>',
                unsafe_allow_html=True,
            )

        comment = st.text_area('Comentário', key='review_comment_input')

        if st.button('Cadastrar', key='review_create_btn'):
            if not comment.strip():
                st.error('O campo comentário não pode estar vazio.')
            else:
                new_review = reviews_service.create_review(
                    movie=movie_titles[selected_movie_title],
                    stars=stars,
                    comment=comment,
                )
                if new_review:
                    st.success(f"Review do filme '{selected_movie_title}' cadastrado com sucesso!")
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar avaliação. Verifique os campos!')
