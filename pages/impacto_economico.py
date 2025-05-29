from common import stream_page_config_start, stream_page_config_end
import streamlit as st
import pandas as pd
import plotly.express as px

# ⬅️ Início da configuração compartilhada
stream_page_config_start()

# ======= DADOS =======
empregos_regiao = pd.DataFrame({
    'Região': ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte'],
    'Empregos': [112000, 48000, 38500, 21000, 16200]
})

pib_musica = pd.DataFrame({
    'Setor': ['Audiovisual', 'Música', 'Design', 'Publicidade', 'Artes visuais', 'Literatura e outros'],
    'Participação (%)': [28, 21, 18, 15, 10, 8]
})

evolucao_empregos = pd.DataFrame({
    'Ano': [2015, 2017, 2019, 2021, 2023],
    'Empregos': [41000, 44500, 48000, 52000, 59200]
})

pib_regional = pd.DataFrame({
    'Região': ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte'],
    'PIB (R$ bilhões)': [35.2, 12.8, 10.4, 6.9, 4.1]
})

# ======= CONTEÚDO DA PÁGINA =======
st.title("📈 O Impacto Econômico da Música no Brasil")

st.image("assets/cantor_publico.jpg", use_container_width=True)

st.markdown("""
### Objetivo
Este painel busca destacar o papel estratégico da música dentro da economia criativa no Brasil, especialmente em termos de geração de empregos e contribuição para o PIB regional, fortalecendo a relevância dos artistas locais e do setor cultural como agentes de desenvolvimento econômico.

---

### Introdução
Num país onde a diversidade musical é um dos maiores patrimônios culturais, a música também se revela como força econômica. Ela emprega milhares de pessoas, movimenta cadeias produtivas e se consolida como setor estratégico da economia criativa, principalmente nas regiões Sudeste e Nordeste.

Entender os números por trás dessa potência cultural é essencial para orientar políticas públicas e ações de fomento à arte e aos artistas locais.
""")

# ======= GRÁFICO 1 =======
st.header("1. Geração de Empregos na Economia Criativa por Região (2023)")
fig1 = px.bar(empregos_regiao, x="Região", y="Empregos", color="Região",
              title="Empregos por Região", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
*O que mostra:* Número de empregos formais na economia criativa por região brasileira.

*Objetivo:* Demonstrar onde estão os maiores polos de emprego.  
*Insight:* O Sudeste concentra a maior parte dos empregos da economia criativa, mas o Nordeste e o Sul também têm participação relevante — o que mostra o potencial de fomento regional.
""")

# ======= GRÁFICO 2 =======
st.header("2. Participação da Música no PIB da Economia Criativa (2023)")
fig2 = px.pie(pib_musica, names="Setor", values="Participação (%)", title="Participação no PIB da Economia Criativa")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
*O que mostra:* A proporção de participação da música em relação a outros setores da economia criativa.

*Objetivo:* Reforçar a relevância econômica da música.  
*Insight:* A música representa mais de 1/5 do PIB criativo, consolidando seu valor não apenas simbólico, mas financeiro.
""")

# ======= GRÁFICO 3 =======
st.header("3. Evolução dos Empregos na Música (2015–2023)")
fig3 = px.line(evolucao_empregos, x="Ano", y="Empregos", markers=True, title="Evolução dos Empregos na Música")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
*O que mostra:* Crescimento dos empregos formais no setor musical ao longo do tempo.

*Objetivo:* Analisar tendências.  
*Insight:* Apesar dos desafios recentes, o setor musical mostra crescimento sustentado, impulsionado pela digitalização e streaming.
""")

# ======= GRÁFICO 4 =======
st.header("4. PIB da Economia Criativa por Região (2023)")
fig4 = px.bar(pib_regional.sort_values(by="PIB (R$ bilhões)", ascending=True),
              x="PIB (R$ bilhões)", y="Região", orientation="h", color="Região",
              title="PIB da Economia Criativa por Região", text_auto=True)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
*O que mostra:* Valores absolutos do PIB da economia criativa por região brasileira.

*Objetivo:* Destacar a concentração e o potencial de expansão.  
*Insight:* O Sudeste lidera, mas o Norte e Nordeste têm espaço para crescer com apoio à produção cultural.
""")

# ======= CONCLUSÃO =======
st.markdown("""
---
### Conclusão

A música é uma engrenagem da economia brasileira. Gera empregos, arrecada impostos, movimenta setores como turismo e tecnologia — mas ainda enfrenta desafios de visibilidade, financiamento e estrutura para os artistas independentes.

Dar visibilidade a esses dados é um passo essencial para promover políticas mais justas e inclusivas, valorizando a produção cultural como vetor de desenvolvimento sustentável.
""")

# ⬇️ Finalização da configuração
stream_page_config_end()
