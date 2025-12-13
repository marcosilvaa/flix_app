import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime

def show_actors():
    actor_serivce = ActorService()
    actors = actor_serivce.get_actors()

    if actors:    
        st.write("Lista de Atores")
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key='actors_grid',
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
        )
    else:
        st.warning("Nenhum Ator/Atriz encontrado")
    
    st.title("Cadastrar novo Ator")
    name = st.text_input('Nome do ator')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1900,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL','USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actor_serivce.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.success(f"Ator '{name}' cadastrado com sucesso!")
            st.rerun()
        else:
            st.error('Erro ao cadastrar Ator/Atriz. Verifique os campos!')