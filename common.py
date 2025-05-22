import pandas as pd
import plotly.express as px

def load_engajamento_dataset()->pd.DataFrame:
    return pd.read_csv('datasets/most_streamed_music_2024.csv',encoding="ISO-8859-1")


def plot_views_pie_chart_engajamento1(df: pd.DataFrame):
    col_views = ['TikTok Views', 'YouTube Views', 'Spotify Streams',
                 'Soundcloud Streams', 'Pandora Streams', 'Shazam Counts']

    # Limpeza dos dados
    for col in col_views:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    # Soma total por plataforma
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Plataforma', 'Total']

    # Plotly Pie Chart
    fig = px.pie(
        somas,
        names='Plataforma',
        values='Total',
        title='Total de Views por Plataforma',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    return fig


import pandas as pd
import plotly.express as px


def plot_views_bar_chart_engajamento2(df: pd.DataFrame):
    col_views = ['TikTok Views', 'YouTube Views', 'Spotify Streams',
                 'Soundcloud Streams', 'Pandora Streams', 'Shazam Counts']

    # Limpeza dos dados
    for col in col_views:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    # Soma total por plataforma
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Plataforma', 'Total']

    # Plotly Bar Chart
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

def plot_tiktok_pie_chart(df: pd.DataFrame):
    col_views = ['TikTok Views', 'TikTok Likes', 'TikTok Posts']

    # Limpeza dos dados
    for col in col_views:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    # Soma total por métrica
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    # Gráfico de pizza com Plotly Express
    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Distribuição TikTok: Views, Likes e Posts',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    return fig


def plot_youtube_pie_chart(df: pd.DataFrame):
    col_views = ['YouTube Views', 'YouTube Likes']

    # Limpeza dos dados
    for col in col_views:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(',', '', regex=False)
                .str.extract(r'(\d+)', expand=False)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove linhas com valores ausentes nas colunas alvo
    df = df.dropna(subset=col_views)

    # Soma total por métrica
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    # Gráfico de pizza com Plotly Express
    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Proporção entre YouTube Views e Likes',
        color_discrete_sequence=px.colors.qualitative.Set3,
    )

    return fig

def plot_spotify_pie_chart(df: pd.DataFrame):
    col_views = ['Spotify Streams', 'Spotify Playlist Reach']

    # Limpeza dos dados
    for col in col_views:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(',', '', regex=False)
                .str.extract(r'(\d+)', expand=False)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove linhas com valores ausentes
    df = df.dropna(subset=col_views)

    # Soma total por métrica
    somas = df[col_views].sum().reset_index()
    somas.columns = ['Métrica', 'Total']

    # Gráfico de pizza com Plotly Express
    fig = px.pie(
        somas,
        names='Métrica',
        values='Total',
        title='Proporção entre Spotify Streams e Playlist Reach',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    return fig




