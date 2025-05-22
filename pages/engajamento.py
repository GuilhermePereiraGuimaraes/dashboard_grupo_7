import numpy as np
import pandas as pd
import streamlit as st
import common

common.stream_page_config_start()
with st.container():
    st.title("Dashboard grupo 7")
    st.image("assets/wallpaper_music.jpg", use_container_width=True)
    df_engajamento = common.load_engajamento_dataset()

    st.write("---- Musicas-chan -----")
    st.header("Quais plataformas mais impactam na visibilidade dos músicos ?")
    st.write("""    O Tiktok detém o maior impacto a respeito da visualização das músicas pois a plataforma foca em vídeos 
                curtos e com um alto poder de propagação, isso facilita a exposição da música para um maior número de 
                pessoas e em pouquíssimo tempo. O gráfico abaixo mostra melhor isso, ele trata das músicas mais tocadas, 
                o Tiktok ganha em disparada na questão de visibilidade justamente por conta da natureza dele ser focada 
                em propagação""")

    fig = common.plot_views_pie_chart_engajamento1(df_engajamento)
    st.plotly_chart(fig,use_container_width=True)

    fig = common.plot_views_bar_chart_engajamento2(df_engajamento)
    st.plotly_chart(fig,use_container_width=True)

    st.header("Quais plataformas entregam um maior engajamento proporcionais ?")
    st.write("""
                O engajamento seria a maneira como a plataforma consegue transformar visualizações em ações reais, como por 
            exemplo: likes, posts, etc. A plataforma que também conseguiu melhor traduzir visualizações em ações foi o 
            TikTok, seguido pelo Spotify e depois o Youtube. O TikTok conseguiu um aproveitamento de quase 10%, isso 
            significa que a cada 10 visualizações uma se convertia em ação, nesse caso a ação era o ato de curtir, 
            também pode se observar que posts representam 0.1% algo muito abaixo que as curtidas, mas que significa que 
            a cada 1000 visualizações uma virava post, isso revela muito da natureza de propagação do TikTok quando se 
            fala de música.""")
    st.write(""" No Youtube apenas 0.7% se tornava curtida, no Spotify não tem uma maneira fácil de calcular engajamento, 
            mas do total de visualizações 5.1% foram via playlist o que também mostra que o Spotify também tem um 
            efeito propagador muito interessante.""")

    fig = common.plot_tiktok_pie_chart(df_engajamento)
    st.plotly_chart(fig,use_container_width=True)

    fig = common.plot_youtube_pie_chart(df_engajamento)
    st.plotly_chart(fig,use_container_width=True)

    fig = common.plot_spotify_pie_chart(df_engajamento)
    st.plotly_chart(fig, use_container_width=True)

common.stream_page_config_end()
