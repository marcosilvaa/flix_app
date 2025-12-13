import streamlit as st 
from login.page import show_login
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def  main():
    
    if 'token' not in st.session_state:
        show_login()
    else:    
        st.title("Flix App")
        st.divider()
        
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início','Gêneros','Atores','Filmes','Avaliações']
        )
        
        if menu_option == 'Início':
            st.write('Início')
            
        if menu_option == 'Gêneros':
            st.write('Gêneros')
            show_genres()
            
            
        if menu_option == 'Atores':
            st.write('Atores')
            show_actors()
        
        if menu_option == 'Filmes':
            st.write('Filmes')
            show_movies()
            
        if menu_option == 'Avaliações':
            st.write('Avaliações')
            show_reviews()
        
if __name__ == '__main__':
    main()