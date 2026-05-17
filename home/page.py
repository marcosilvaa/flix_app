import streamlit as st
import plotly.express as px

from movies.services import MovieService


def show_home():
    movie_service = MovieService()

    with st.spinner('Carregando estatísticas...'):
        movie_stats = movie_service.get_movie_stats()

    if not movie_stats:
        st.error('Não foi possível carregar as estatísticas. Tente novamente.')
        return

    total_movies = movie_stats.get('total_movies', 0)
    total_reviews = movie_stats.get('total_reviews', 0)
    average_stars = movie_stats.get('average_stars', 0)
    movies_by_genre = movie_stats.get('movies_by_genre', [])

    st.title('Painel de Estatísticas')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='Filmes Cadastrados', value=total_movies)
    with col2:
        st.metric(label='Avaliações', value=total_reviews)
    with col3:
        stars_display = f'{average_stars:.1f} / 5.0' if average_stars else '—'
        st.metric(label='Média de Estrelas', value=stars_display)

    st.divider()

    if movies_by_genre:
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.subheader('Filmes por Gênero')
            fig_pie = px.pie(
                movies_by_genre,
                values='count',
                names='genre__name',
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            fig_pie.update_layout(
                showlegend=True,
                margin=dict(t=20, b=20, l=20, r=20),
                height=400,
            )
            fig_pie.update_traces(
                textposition='inside',
                textinfo='percent+label',
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with col_chart2:
            st.subheader('Quantidade por Gênero')
            fig_bar = px.bar(
                movies_by_genre,
                x='genre__name',
                y='count',
                color='genre__name',
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            fig_bar.update_layout(
                xaxis_title='Gênero',
                yaxis_title='Quantidade',
                showlegend=False,
                margin=dict(t=20, b=20, l=20, r=20),
                height=400,
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info('Nenhum dado de gêneros disponível para exibir gráficos.')

    st.divider()

    if total_reviews > 0 and average_stars:
        st.subheader('Média de Avaliações')
        star_full = int(average_stars)
        star_half = 1 if (average_stars - star_full) >= 0.5 else 0
        star_empty = 5 - star_full - star_half
        stars_visual = '★' * star_full + '½' * star_half + '☆' * star_empty
        st.markdown(
            f'<span style="font-size:2.5em; color:#FFD700;">{stars_visual}</span>'
            f' <span style="font-size:1.5em; vertical-align:middle;">{average_stars:.1f} / 5.0</span>',
            unsafe_allow_html=True,
        )

    if movies_by_genre:
        st.divider()
        st.subheader('Resumo por Gênero')
        for genre in movies_by_genre:
            st.write(f"• **{genre['genre__name']}**: {genre['count']} filme(s)")
