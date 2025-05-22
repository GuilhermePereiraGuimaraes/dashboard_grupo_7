import numpy as np
import pandas as pd
import streamlit as st
import common

with st.sidebar:
    st.write("Engajamento")

with st.container():
    st.title("Dashboard grupo 7")
    st.image("assets/wallpaper_music.jpg")
    df_engajamento = common.load_engajamento_dataset()

    st.write("---- Dashboard engajamento 1 -----")
    st.header("Grafico torta")

    fig = common.plot_views_pie_chart_engajamento1(df_engajamento)
    st.plotly_chart(fig)

    st.header("Grafico torta 2")

    fig = common.plot_views_bar_chart_engajamento2(df_engajamento)
    st.plotly_chart(fig)

    fig = common.plot_tiktok_pie_chart(df_engajamento)
    st.plotly_chart(fig)

    fig = common.plot_youtube_pie_chart(df_engajamento)
    st.plotly_chart(fig)

    fig = common.plot_spotify_pie_chart(df_engajamento)
    st.plotly_chart(fig)

