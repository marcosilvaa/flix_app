import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


movies = [
    {
        'id':1,
        'name':'Rock N Hola'
    }
]

def show_movies():
    st.write("Lista de Filmes")

    AgGrid(
        data=pd.DataFrame(movies),
        key='movies_grid',
        reload=True
    )
    
    st.title("Cadastrar novo Filme")
    name = st.text_input('Nome do Filme')
    if st.button('Cadastrar'):
        st.success(f"Filme '{name}' cadastrado com sucesso!")