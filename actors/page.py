import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

actors = [
    {
        'id':1,
        'name':'Gerard Butler'
    }
]

def show_actors():
    st.write("Lista de Atores")
    
    AgGrid(
        data=pd.DataFrame(actors),
        key='actors_grid',
        reload=True
    )
    
    st.title("Cadastrar novo Ator")
    name = st.text_input('Nome do ator')
    if st.button('Cadastrar'):
        st.success(f"Ator '{name}' cadastrado com sucesso!")