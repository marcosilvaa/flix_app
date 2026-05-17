import streamlit as st
from login.page import show_login
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home


def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        with st.sidebar:
            st.image(
                'https://img.icons8.com/fluency/96/movie-projector.png',
                width=64,
            )
            st.title('Flix App')
            menu_option = st.radio(
                'Navegação',
                ['Início', 'Gêneros', 'Atores', 'Filmes', 'Avaliações'],
                format_func=lambda x: {
                    'Início': '🏠 Início',
                    'Gêneros': '🎭 Gêneros',
                    'Atores': '🎬 Atores',
                    'Filmes': '🎥 Filmes',
                    'Avaliações': '⭐ Avaliações',
                }[x],
            )
            st.divider()
            if st.button('Sair', use_container_width=True):
                from login.service import logout
                logout()

        if menu_option == 'Início':
            show_home()

        elif menu_option == 'Gêneros':
            show_genres()

        elif menu_option == 'Atores':
            show_actors()

        elif menu_option == 'Filmes':
            show_movies()

        elif menu_option == 'Avaliações':
            show_reviews()


if __name__ == '__main__':
    main()
