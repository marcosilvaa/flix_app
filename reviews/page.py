import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


reviews = [
    {
        'id':1,
        'stars':5
    }
]

def show_reviews():
    st.write("Lista de avaliações")

    AgGrid(
        data=pd.DataFrame(reviews),
        key='movies_grid',
        reload=True
    )
    
    st.title("Cadastrar nova Review")
    name = st.text_input('Nota da Avaliação')
    if st.button('Cadastrar'):
        st.success(f"Review nota '{name}' cadastrado com sucesso!")