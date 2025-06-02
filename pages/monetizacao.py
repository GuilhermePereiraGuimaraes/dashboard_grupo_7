import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os
import common 

common.stream_page_config_start()
#  Configuração inicial
# st.set_page_config(page_title="Monetização", layout="wide")

#  Cabeçalho centralizado
st.markdown("<h1 style='text-align: center;'>Monetização dos Artistas Brasileiros</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; max-width: 850px; margin: 0 auto;'>
A indústria musical passou por grandes transformações com o avanço das plataformas de streaming. Este painel investiga os principais canais de receita disponíveis para artistas brasileiros, com foco especial no pagamento por stream e no potencial de alcance de cada plataforma.
</div>
""", unsafe_allow_html=True)

# Caminho do CSV com os dados
# base_path = os.path.dirname(os.path.dirname(__file__))
# file_path = os.path.join(base_path, "streaming_pagamento.csv.csv")
file_path = "datasets/streaming_pagamento.csv.csv"

# Dados fixos: usuários ativos por plataforma (em milhões)
usuarios_data = {
    "Plataforma": [
        "Spotify", "Apple Music", "Amazon Music", "YouTube Music", "Deezer", "Tidal", "Napster"
    ],
    "Usuários Ativos (milhões)": [602, 110, 82, 80, 16, 5, 3]
}
df_usuarios = pd.DataFrame(usuarios_data)

# Carregar dados e apresentar texto + gráficos
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df = df.drop(columns=["Ano da Estimativa"], errors="ignore")
    df = pd.merge(df, df_usuarios, on="Plataforma", how="left")

    # Texto introdutório
    st.markdown("---")
    st.markdown("""
### Quais plataformas mais recompensam financeiramente os artistas?

A remuneração por stream varia bastante entre as plataformas. O Napster, por exemplo, oferece a maior média de pagamento por reprodução, em torno de **USD 0.01**. Em contrapartida, o YouTube Music, com uma base de usuários muito maior, paga menos de **USD 0.002** por stream.

A média geral entre as plataformas analisadas gira em torno de **USD 0.008**, o que reforça a ideia de que apenas o volume de reprodução não garante sustentabilidade para um artista; o valor pago também importa.
""")


    fig, ax = plt.subplots(figsize=(6, 2.7))
    ax.bar(df['Plataforma'], df['Pagamento por Stream (USD)'], color='skyblue')
    ax.set_xlabel("Plataforma")
    ax.set_ylabel("USD por Stream")
    ax.set_title("Pagamento por Stream")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.markdown("""
### Quantidade de ouvintes importa?

Embora o valor por stream seja relevante, a **quantidade de usuários ativos** também é determinante. Por isso, artistas precisam avaliar onde estão os ouvintes e o quão bem cada reprodução é monetizada.

O gráfico abaixo mostra a base de usuários ativos de cada plataforma, permitindo comparar volume com remuneração.
""")

    fig_users = px.bar(
        df.sort_values("Usuários Ativos (milhões)", ascending=False),
        x="Plataforma", y="Usuários Ativos (milhões)",
        color="Plataforma", title="", height=350
    )
    fig_users.update_layout(showlegend=False)
    st.plotly_chart(fig_users, use_container_width=True)

    st.markdown("""
### Existe equilíbrio entre visibilidade e retorno?

As plataformas que mais pagam por stream não são, necessariamente, as mais populares. O gráfico a seguir mostra a **correlação entre o pagamento por reprodução e o número de usuários ativos**.

Isso ajuda a entender o dilema de muitos artistas: vale mais estar onde se é mais ouvido ou onde se é melhor pago?
""")

    # Gráfico 3 - Dispersão: usuários x pagamento
    scatter = px.scatter(
        df,
        x="Usuários Ativos (milhões)", y="Pagamento por Stream (USD)",
        size="Pagamento por Stream (USD)", color="Plataforma",
        hover_name="Plataforma", height=400
    )
    scatter.update_layout(showlegend=False)
    st.plotly_chart(scatter, use_container_width=True)

    st.markdown("---")
    st.markdown("""
### Considerações Finais

O Napster e o Tidal são exemplos claros de plataformas com alto valor por stream, mas baixa base de usuários. Já o Spotify e o YouTube dominam em número de ouvintes, porém oferecem valores muito baixos por reprodução.

Na prática, os artistas brasileiros precisam **diversificar canais de receita**: plataformas digitais, eventos ao vivo, editais públicos e merchandising continuam essenciais para garantir sustentabilidade financeira.
""")

else:
    st.warning(f"⚠️ Arquivo de dados '{file_path}' não encontrado. Verifique o caminho.")

st.markdown("<p style='text-align: center; font-size: 0.9em;'>Grupo 7 GTI 2025</p>", unsafe_allow_html=True)
common.stream_page_config_end()