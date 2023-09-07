import pandas as pd
# import basedosdados as bd
import streamlit as st
import os
print(os.getcwd())

st.set_page_config(
    page_title="Estatísticas",
    page_icon = ":⚽:",
    layout="wide"
)

# Para carregar o dado direto no pandas
if "data" not in st.session_state:
    # df_databigquery = bd.read_table(dataset_id='mundo_transfermarkt_competicoes',
    # table_id='brasileirao_serie_a',
    # billing_project_id="projfutebol")
    # st.session_state["data"] = df_databigquery

    df_brasFul = pd.read_csv('pages/campeonato-brasileiro-full.csv')
    st.session_state["dataBrasFull"] = df_brasFul

    df_brasGols = pd.read_csv('pages/campeonato-brasileiro-gols.csv')
    st.session_state["dataBrasGols"] = df_brasGols

    df_data = pd.read_csv('pages/df_Big_query.csv')
    st.session_state["data"] = df_data

    df_brasCards = pd.read_csv('pages/campeonato-brasileiro-cartoes.csv')
    st.session_state["dataBrasCards"] = df_brasCards

    df_brasPosition = pd.read_csv('pages/pirmeiros_colocados.csv')
    st.session_state["df_brasPosition"] = df_brasPosition

st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")

logo = "https://upload.wikimedia.org/wikipedia/pt/thumb/4/42/Campeonato_Brasileiro_S%C3%A9rie_A_logo.png/109px-Campeonato_Brasileiro_S%C3%A9rie_A_logo.png?20160723160542"
col1, col2, col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.markdown("<h1 style='text-align: center;'>Campeonato Brasileiro</h1>", unsafe_allow_html=True)
st.write('''
Este projeto foi criado utilizando as bases de dados disponíveis nos sites Base dos Dados e no kaggle, foi construído em Python utilizando bibliotecas Pandas, Streamlit e Numpy.
''')
st.write("Pode ser que alguns dados apresentem divergências, isto porque as planilhas que estão sendo utilizadas, estão com muitos dados faltantes, mas se achou alguma coisa, chama no linkedin e me informe as falhas para que possamos construir algo bem interessante")

st.write("Acesse a base dos dados clicando neste [link](https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa)")

st.write('Acesse os dados do Kaggle clicando neste [link](https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol)')

st.write('Aqui vou trazer estatísticas e dados do campeonato brasileiro, a ideia é que com o tempo consiga buscar informações perdidas no tempo para alimentar as planilhas e tenhamos um trabalho mais completo.')

st.write('Acesse a barra lateral na setinha acima " > " e confira tudo o que já está sendo realizado.')