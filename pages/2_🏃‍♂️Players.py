import streamlit as st

st.set_page_config(
    layout='wide',
    page_title= 'Players',
    page_icon="🏃‍♂️"
)


# Verifica se 'data' está inicializado no session_state
if 'data' not in st.session_state:
    st.error("Os dados não foram carregados. Volte para a página principal!")
else:
    df_data = st.session_state['data']


clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("CLubes", clubes)

df_player = df_data[df_data['Club'] == club]

players = df_data['Name'].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4, col5, col6 = st.columns(6) 
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura (M):** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso (Kg):** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
col4.markdown(
    "<div style='text-align: center;'><strong>-</strong></div>",
    unsafe_allow_html=True
)
col5.markdown(
    "<div style='text-align: center;'><strong>-</strong></div>",
    unsafe_allow_html=True
)
col6.markdown(
    "<div style='text-align: center;'><strong>-</strong></div>",
    unsafe_allow_html=True
)
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))
col1, col2, col3, col4 = st.columns(4) 
col1.metric(label='Valor de Mercado', value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label='Remuneração Semanal', value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label='Cláusula de Recisão', value=f"£ {player_stats['Release Clause(£)']:,}")

