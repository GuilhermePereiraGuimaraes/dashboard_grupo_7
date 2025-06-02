
import streamlit as st
import pandas as pd
import plotly.express as px
import unicodedata
import json
import requests
import common

def main():
    common.stream_page_config_start()
    # st.set_page_config(page_title="Gêneros Musicais e Distribuição dos Artistas no Brasil", layout="wide")
    st.title("🎶 Quais são os gêneros musicais e a distribuição geográfica dos principais artistas em atividade no Brasil?")

    st.markdown("""
    Quem são os nomes mais ouvidos da música brasileira hoje?  
    Este painel mostra os artistas em destaque nas plataformas digitais, organizados por popularidade, gênero musical e região de atuação.  
    Acompanhe como a produção musical brasileira se manifesta em diferentes territórios e conheça o perfil dos artistas que fazem parte da cena independente e regional.
    """)

    caminho_arquivo = "datasets/artista.csv"
    try:
        df = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado no caminho especificado: {caminho_arquivo}")
        st.stop()

    # Renomear colunas para formato padronizado
    rename_dict = {
        'Posição': 'Posicao',
        'Gênero': 'Genero',
        'Localização': 'Localizacao'
    }
    df.rename(columns=rename_dict, inplace=True)

    # Confirmar colunas obrigatórias
    colunas_esperadas = ['Posicao', 'Artista', 'Genero', 'Localizacao', 'Onda']
    if not all(col in df.columns for col in colunas_esperadas):
        st.error(f"Erro: As colunas esperadas não foram encontradas no arquivo. Esperadas: {colunas_esperadas}")
        st.stop()

    # Indicadores principais
    try:
        artista_top = df.loc[df['Posicao'] == 1, 'Artista'].values[0]
    except:
        artista_top = 'Não encontrado'

    genero_mais_frequente = df['Genero'].mode()[0]

    st.markdown("### 📌 Indicadores de Destaque")
    col1, col2 = st.columns(2)
    col1.metric("🎧 Artista mais ouvido no Brasil em 2024", artista_top)
    col2.metric("🎼 Gênero musical mais presente nos estados", genero_mais_frequente)

    st.markdown("---")

    # 1. Ranking Nacional de Artistas
    st.subheader("📊 1. Ranking Nacional de Artistas")
    st.markdown("Top 20 artistas brasileiros mais populares nas plataformas. Esta visualização apresenta os artistas com maior volume de streams no cenário nacional, com base nos dados mais recentes das plataformas de música.")

    top_20 = df.sort_values("Posicao").head(20)
    st.dataframe(top_20[['Posicao', 'Artista', 'Genero', 'Localizacao']].reset_index(drop=True))

    st.markdown("---")

    # 2. Mapa Interativo
    st.subheader("🗺️ 2. Mapa Interativo: Distribuição Geográfica dos Gêneros mais escutados")
    st.markdown("O que as regiões estão escutando? Mapeamos os gêneros em destaque por região brasileira para entender como a produção musical se espalha pelo território nacional.")

    if ' - ' in df['Localizacao'].iloc[0]:
        df[['Cidade', 'Estado']] = df['Localizacao'].str.split(' - ', expand=True)
    else:
        df['Estado'] = df['Localizacao']

    geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
    response = requests.get(geojson_url)
    br_states = response.json()

    estado_map = {
        'Acre': 'AC', 'Alagoas': 'AL', 'Amapa': 'AP', 'Amazonas': 'AM', 'Bahia': 'BA', 'Ceara': 'CE',
        'Distrito Federal': 'DF', 'Espirito Santo': 'ES', 'Goias': 'GO', 'Maranhao': 'MA', 'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS', 'Minas Gerais': 'MG', 'Para': 'PA', 'Paraiba': 'PB', 'Parana': 'PR',
        'Pernambuco': 'PE', 'Piaui': 'PI', 'Rio de Janeiro': 'RJ', 'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS', 'Rondonia': 'RO', 'Roraima': 'RR', 'Santa Catarina': 'SC',
        'Sao Paulo': 'SP', 'Sergipe': 'SE', 'Tocantins': 'TO'
    }

    genero_estado = df.groupby('Estado')['Genero'].agg(lambda x: x.mode()[0]).reset_index()
    genero_estado['Estado'] = genero_estado['Estado'].map(lambda x: estado_map.get(x.strip(), x.strip()))

    fig_map = px.choropleth_mapbox(
        genero_estado,
        geojson=br_states,
        locations='Estado',
        color='Genero',
        featureidkey="properties.sigla",
        center={"lat": -14.5, "lon": -52},
        mapbox_style="carto-positron",
        zoom=3.5,
        title='Gênero mais escutado por estado'
    )
    st.plotly_chart(fig_map, use_container_width=True)

    st.markdown("---")

    # 3. Gêneros Musicais em Alta
    st.subheader("🎵 3. Gêneros Musicais em Alta")
    st.markdown("Quais estilos estão conquistando o público? Esta análise ajuda a compreender as tendências do gosto musical no país e oferece referências para novos artistas se posicionarem.")

    genero_count = df['Genero'].value_counts().reset_index()
    genero_count.columns = ['Genero', 'Numero de Artistas']
    fig_genero = px.bar(genero_count, x='Genero', y='Numero de Artistas', color='Genero')
    st.plotly_chart(fig_genero, use_container_width=True)

    st.markdown("---")

    # 4. Evolução da Popularidade
    st.subheader("📈 4. Evolução da Popularidade dos Artistas")
    st.markdown("Para mais detalhes é possível comparar a trajetória dos artistas ao longo do tempo com base no volume de streams mensais.")

    artistas_selecionados = st.multiselect(
        "Selecione até 5 artistas para comparar:",
        df['Artista'].unique(),
        max_selections=5
    )

    if artistas_selecionados:
        df_filtrado = df[df['Artista'].isin(artistas_selecionados)]
        fig_evolucao = px.line(
            df_filtrado,
            x='Posicao',
            y='Onda',
            color='Artista',
            markers=True,
            labels={'Onda': 'Streams (proxy)', 'Posicao': 'Ranking'},
            title='Comparativo de Popularidade por Posição'
        )
        st.plotly_chart(fig_evolucao, use_container_width=True)
    common.stream_page_config_end()


if __name__ == '__main__':
    main()
