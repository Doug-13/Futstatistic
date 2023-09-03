import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# doug-mello@projfutebol.iam.gserviceaccount.com
# Importar funções
# from ..utilitarios.funct import get_club_logo
# from ..utilitarios.funct import get_club_color

st.set_page_config(
    page_title="Estatísticas",
    page_icon = ":⚽:",
    layout="wide"
)

df_data = st.session_state["data"]
df_brasGols = st.session_state["dataBrasGols"]
df_brasFul = st.session_state["dataBrasFull"]
df_brasCards = st.session_state["dataBrasCards"]



# Criar caixa de seleção de Ano
years = sorted(df_data["ano_campeonato"].value_counts().index, reverse=True)
year = st.sidebar.selectbox("Ano", years)


st.title("Estatísticas por Campeonato")
st.write("Página em construção")

st.image('https://contajul.com/site/wp-content/uploads/retencao-na-construcao-civil.jpg ',width=440)