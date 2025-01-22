import streamlit as st
import pandas as pd
from datetime import datetime

#tecnica de carregamento do state e distribuicao disso nas outras paginas (cacheamento)
#Um recurso do Streamlit que permite armazenar e compartilhar dados entre interações dentro do aplicativo. 
# Funciona como uma memória persistente enquanto a aplicação está em execução.
if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year] #filtro de contrato válido
    df_data = df_data[df_data["Value(£)"] > 0] #filtro de valor de mercado
    df_data = df_data.sort_values(by="Overall", ascending=False) #ordena dataframe com base na coluna Overall de forma decrescente (melhor para pior)
    st.session_state["data"] = df_data #Armazena dataframe filtrado e processado na chave data


st.markdown("#FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Grupo Gali](https://galileunegocios.com.br/)")


btn = st.link_button("Acesse os dados do Kaggle", "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database" ) 

st.markdown("""
            The dataset contains +17k unique players and more than 60 columns, general information 
            and all KPIs the famous videogame offers. As the esport scene keeps rising espacially on FIFA, 
            I thought it can be useful for the community (kagglers and/or gamers))""")
