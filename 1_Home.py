import pandas as pd
import basedosdados as bd
import streamlit as st

# Para carregar o dado direto no pandas
if "data" not in st.session_state:
    df_data = bd.read_table(dataset_id='mundo_transfermarkt_competicoes',
    table_id='brasileirao_serie_a',
    billing_project_id="projfutebol")
    st.session_state["data"] = df_data

    df_brasFul = pd.read_csv('Arquivos\campeonato-brasileiro-full.csv')
    st.session_state["dataBrasFull"] = df_brasFul

    df_brasGols = pd.read_csv('Arquivos\campeonato-brasileiro-gols.csv')
    st.session_state["dataBrasGols"] = df_brasGols

    df_brasCards = pd.read_csv('Arquivos\campeonato-brasileiro-cartoes.csv')
    st.session_state["dataBrasCards"] = df_brasCards


st.header('**Dados Campeonato Brasileiro**')
 
st.write('''
Este projeto foi criado utilizando as bases de dados disponíveis nos sites Base dos Dados e no kaggle, foi construído em Python utilizando bibliotecas Pandas, Streamlit e Numpy.
''')

st.write("Acesse a base dos dados clicando neste [link](https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa)")

st.write('Acesse os dados do Kaggle clicando neste [link](https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol)')