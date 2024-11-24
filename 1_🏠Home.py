import streamlit as st
import webbrowser as wb
import pandas as pd
from datetime import datetime

st.set_page_config(
    layout='wide'
)

if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data


st.markdown('# FIFA 2023 OFICIAL DATASET!')
st.sidebar.markdown('Desenvolvido por [Willian Murakami](https://www.linkedin.com/in/willian-murakami/)')



btn = st.link_button(
    'acesse os dados no kaggle',
    'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    O conjunto de dados do jogador de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissional. 
    
    **O conjunto de dados contém uma ampla gama de atributos**, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes. Com mais de 17.000 registros, esse conjunto de dados oferece um recurso valioso para analistas, pesquisadores e entusiastas do futebol interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.
""")

