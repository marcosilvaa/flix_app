import streamlit as st 
import requests
from login.service import logout


class GenreRepository:
     
    def __init__(self):
        self.__base_url = 'https://marcosilva.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }
        
        
    def get_genres(self):
        response = requests.get(
            self.__auth_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Cod: {response.status_code}')
    
    
    def create_genre(self, genre):
        response = requests.post(
            self.__auth_url,
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Cod: {response.status_code}')