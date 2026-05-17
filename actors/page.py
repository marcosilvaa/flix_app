import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, AgGridTheme
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.subheader('Atores Cadastrados')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            actors_df,
            theme=AgGridTheme.STREAMLIT,
            key='actors_grid',
            reload_data=True,
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado')

    st.divider()

    with st.expander('Cadastrar novo Ator', expanded=not actors):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Nome do Ator', key='actor_name_input')
        with col2:
            nationality = st.selectbox(
                label='Nacionalidade',
                options=['BRAZIL', 'USA'],
                key='actor_nationality_input',
            )

        birthday = st.date_input(
            label='Data de Nascimento',
            value=datetime(2000, 1, 1).date(),
            min_value=datetime(1900, 1, 1).date(),
            max_value=datetime.today(),
            format='DD/MM/YYYY',
            key='actor_birthday_input',
        )

        if st.button('Cadastrar', key='actor_create_btn'):
            if not name:
                st.error('O campo nome não pode estar vazio.')
            else:
                new_actor = actor_service.create_actor(
                    name=name,
                    birthday=birthday,
                    nationality=nationality
                )
                if new_actor:
                    st.success(f"Ator '{name}' cadastrado com sucesso!")
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar Ator/Atriz. Verifique os campos!')
