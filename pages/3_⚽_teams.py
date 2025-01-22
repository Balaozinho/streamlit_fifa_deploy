import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"] #carrega as informações do session state

clubes = df_data["Club"].value_counts().index #carrega clubes únicos no dataframe
club = st.sidebar.selectbox("Clube", clubes) #menu suspenso onde o label é Clube e a lista de clubes é *clubes*

#filtrando o dataframe e ajustando o índice de número para name
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")  #"set_index": Substitui o índice padrão do Pandas (numérico, baseado na posição das linhas) pela coluna "Name"

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)","Wage(£)",
           "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
            column_config={
                "Overall": st.column_config.ProgressColumn(
                    "Overall", format="%d", min_value=0, max_value=100
                ),"Wage(£)": st.column_config.ProgressColumn(
                    "Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")

            })