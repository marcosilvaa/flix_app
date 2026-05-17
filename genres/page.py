import streamlit as st
from st_aggrid import AgGrid, AgGridTheme
import pandas as pd
from genres.service import GenreService


def show_genres():

    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.subheader('Gêneros Cadastrados')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            genres_df,
            theme=AgGridTheme.STREAMLIT,
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado!')

    st.divider()

    with st.expander('Cadastrar novo Gênero', expanded=not genres):
        name = st.text_input('Nome do Gênero', key='genre_name_input')
        if st.button('Cadastrar', key='genre_create_btn'):
            if not name:
                st.error('O campo nome não pode estar vazio.')
            else:
                existing_genres = {g['name'].lower() for g in genres} if genres else set()

                if name.lower() in existing_genres:
                    st.error(f'O gênero "{name}" já existe!')
                else:
                    new_genre = genre_service.create_genre(
                        name=name
                    )
                    if new_genre:
                        st.success(f'Gênero: {name} cadastrado com sucesso!')
                        st.rerun()
                    else:
                        st.error('Erro ao cadastrar o Gênero. Verifique os campos')
