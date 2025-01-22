import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"] #carrega o dataframe df_data a partir do st.session_state

clubes = df_data["Club"].value_counts().index #extrai lista de clubes únicos no arquivo csv
club = st.sidebar.selectbox("Clube", clubes) #cria um menu suspenso, Parametro1: Texto que vamos ver no dah e P2: Lista de clubes únicos

df_players = df_data[(df_data["Club"] == club)] #Filtra o DataFrame para incluir apenas os jogadores que pertencem ao clube selecionado.
#df_data["Club"] == club  , cria mascara booleana para identificar as linhas onde o clube corresponde à seleção do usuário
#df_data[...] , mantém apenas as linhas onde a mascara é True

players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0] #indexador posicional do pandar 

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")


col1, col2, col3, col4 = st.columns(4) #dividir página em 4 colunas
#depois de usar iloc, dá para acessar os atributos daquele Name que foi selecionado
col1.markdown(f"**Idade:** {player_stats['Age']}") #atributo age
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] /100}") #atributo Altura
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}") #atributo peso
st.divider()

st.subheader(f"Overall {player_stats['Overall']}") #atributo overall
st.progress(int(player_stats["Overall"])) #barra de progresso

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}") # ":," é um separador de milhares no formato padrão global
col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="CLaúsula de Rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")


