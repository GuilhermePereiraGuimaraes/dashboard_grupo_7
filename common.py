import pandas as pd
import plotly.express as px
import streamlit as st

# Configuração de layout da página
def stream_page_config_start():
    st.set_page_config(
        page_title="Dashboard Grupo 7",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )

    st.sidebar.title("Navegação")
    st.sidebar.page_link("app.py", label="🏠 Início")
    st.sidebar.page_link("pages/engajamento.py", label="📊 Engajamento")
    st.sidebar.page_link("pages/impacto_economico.py", label="📈 Impacto econômico")



# Ocultar menu lateral (opcional)
def stream_page_config_end():
    hide_sidebar = """
        <style>
        [data-testid="stSidebarNav"] { display: none; }
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Carregamento do dataset
@st.cache_data
def load_engajamento_dataset() -> pd.DataFrame:
    try:
        return pd.read_csv('datasets/most_streamed_music_2024.csv', encoding="ISO-8859-1")
    except Exception as e:
        st.error(f"Erro ao carregar o dataset: {e}")
        st.stop()

# Gráfico de pizza: Views totais por plataforma
def plot_views_pie_chart_engajamento1(df: pd.DataFrame):
    col_views = ['TikTok Views', 'YouTube Views', 'Spotify Streams',
                 'Soundcloud Streams', 'Pandora Streams', 'Shazam Counts']

    df[col_views] = df[col_views].apply(lambda col: pd.to_numeric(col.astype(str).str.replace(',', ''), errors='coerce'))
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Plataforma', 'Total']

    fig = px.pie(
        somas,
        names='Plataforma',
        values='Total',
        title='Total de Views por Plataforma',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig

# Gráfico de barras: Views totais por plataforma
def plot_views_bar_chart_engajamento2(df: pd.DataFrame):
    col_views = ['TikTok Views', 'YouTube Views', 'Spotify Streams',
                 'Soundcloud Streams', 'Pandora Streams', 'Shazam Counts']

    df[col_views] = df[col_views].apply(lambda col: pd.to_numeric(col.astype(str).str.replace(',', ''), errors='coerce'))
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Plataforma', 'Total']

    fig = px.bar(
        somas,
        x='Plataforma',
        y='Total',
        title='Total de Views por Plataforma',
        labels={'Total': 'Total de Views'},
        text_auto=True,
        color='Plataforma',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

# Gráfico TikTok: Views, Likes e Posts
def plot_tiktok_pie_chart(df: pd.DataFrame):
    col_views = ['TikTok Views', 'TikTok Likes', 'TikTok Posts']

    df[col_views] = df[col_views].apply(lambda col: pd.to_numeric(col.astype(str).str.replace(',', ''), errors='coerce'))
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Distribuição TikTok: Views, Likes e Posts',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig

# Gráfico YouTube: Views e Likes
def plot_youtube_pie_chart(df: pd.DataFrame):
    col_views = ['YouTube Views', 'YouTube Likes']

    for col in col_views:
        df[col] = pd.to_numeric(
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.extract(r'(\d+)', expand=False),
            errors='coerce'
        )
    df = df.dropna(subset=col_views)
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Proporção entre YouTube Views e Likes',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig

# Gráfico Spotify: Streams e Playlist Reach
def plot_spotify_pie_chart(df: pd.DataFrame):
    col_views = ['Spotify Streams', 'Spotify Playlist Reach']

    for col in col_views:
        df[col] = pd.to_numeric(
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.extract(r'(\d+)', expand=False),
            errors='coerce'
        )
    df = df.dropna(subset=col_views)
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Proporção entre Spotify Streams e Playlist Reach',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig
