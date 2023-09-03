import pandas as pd
# import basedosdados as bd
import streamlit as st

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

    df_data = pd.read_csv('Arquivos\DF - Big query.csv')
    st.session_state["data"] = df_data

    df_brasFul = pd.read_csv('Arquivos\campeonato-brasileiro-full.csv')
    st.session_state["dataBrasFull"] = df_brasFul

    df_brasGols = pd.read_csv('Arquivos\campeonato-brasileiro-gols.csv')
    st.session_state["dataBrasGols"] = df_brasGols

    df_brasCards = pd.read_csv('Arquivos\campeonato-brasileiro-cartoes.csv')
    st.session_state["dataBrasCards"] = df_brasCards

st.sidebar.markdown('''
# Me siga lá!!
- [Linkedin](https://www.linkedin.com/in/douglas-mello-13b70012a/)
- [Github](https://github.com/Doug-13)
''', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)    
with col1:
    st.image('https://media.licdn.com/dms/image/D4D03AQHfCsdexLdO0A/profile-displayphoto-shrink_100_100/0/1682550966648?e=1698883200&v=beta&t=vy3Qm5QmRQIh-Llg2EE6vm4ouRJMr-24VoJ18zi5jg8', width=140)
with col2:
    st.header('Sobre mim')
st.write('''
Olá, feliz por você estar aqui conhecendo este projeto, meu nome é Douglas, sou apaixonado por programação e análise de dados, 
        sou inquieto e sempre procurando aprender algo novo, gostou, manda dicas aí para aperfeiçoarmos este trabalho! ''')
st.write('''Me segue lá no [Linkedin](https://www.linkedin.com/in/douglas-mello-13b70012a/), e me fala o que achou do projeto, ainda está um pouco bagunçado, mas vai melhorar...''')
st.write(''' Ahhhhh e divulga aí, me ajuda a fazer com que este projeto chegue mais longe!!''')

st.divider()

st.header('**Dados Campeonato Brasileiro**')
st.write('''
Este projeto foi criado utilizando as bases de dados disponíveis nos sites Base dos Dados e no kaggle, foi construído em Python utilizando bibliotecas Pandas, Streamlit e Numpy.
''')
st.write("Pode ser que alguns dados apresentem divergências, isto porque as planilhas que estão sendo utilizadas, estão com muitos dados faltantes, mas se achou alguma coisa, chama no linkedin e me informe as falhas para que possamos construir algo bem interessante")

st.write("Acesse a base dos dados clicando neste [link](https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa)")

st.write('Acesse os dados do Kaggle clicando neste [link](https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol)')