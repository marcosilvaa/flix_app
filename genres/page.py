import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


genres = [
    {
        'id':1,
        'name':'Ação'
    },
    {
        'id':2,
        'name':'Comédia'
    }
]


def show_genres():
    st.write("Lista de Gêneros")
    
    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
        )
    
    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button("Cadastrar"):
        st.success(f'Gênero: {name} cadastrado com sucesso!')
