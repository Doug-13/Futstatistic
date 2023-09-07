import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")

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
logo = "https://upload.wikimedia.org/wikipedia/pt/thumb/4/42/Campeonato_Brasileiro_S%C3%A9rie_A_logo.png/109px-Campeonato_Brasileiro_S%C3%A9rie_A_logo.png?20160723160542"
col1, col2, col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.markdown("<h1 style='text-align: center;'>Campeonato Brasileiro</h1>", unsafe_allow_html=True)

years = sorted(df_data["ano_campeonato"].value_counts().index, reverse=True)
year = st.selectbox("Escolha o Ano", years)

def create_cont_results_general(df_data, year):
    df_clubMan = df_data[
        (df_data["ano_campeonato"] == year)
    ]
    df_clubVis = df_data[
        (df_data["ano_campeonato"] == year)
    ]
    vic_man = len(df_clubMan[df_clubMan["gols_man"] > df_clubMan["gols_vis"]])
    vic_vis = len(df_clubVis[df_clubVis["gols_vis"] > df_clubVis["gols_man"]])
    
    # total de gols marcados
    gols_marc = (df_clubMan["gols_man"].sum()) + (df_clubMan["gols_vis"].sum())
    gols_marc = str(int(gols_marc))
    # gols mandantes
    gols_man = (df_clubMan["gols_man"].sum())
    gols_man= str(int(gols_man))
    # gols visitantes
    gols_vis = (df_clubMan["gols_vis"].sum()) 
    gols_vis= str(int(gols_vis))

    empat = len(df_clubMan[df_clubMan["gols_man"] == df_clubMan["gols_vis"]])
    
    return vic_man,vic_vis,gols_marc,gols_man,gols_vis,empat

vic_man,vic_vis,gols_marc,gols_man,gols_vis,empat= create_cont_results_general(df_data, year)



def localId(df_brasFul,year):
    if year == 2020:
        df_brasFul["data"] = pd.to_datetime(df_brasFul["data"], format="%d/%m/%Y")
        df_year = df_brasFul[df_brasFul["data"].dt.year == year].copy()
        min_id = df_year["ID"].astype(int).min()
        df_jogosCamp = df_brasFul[df_brasFul["ID"].astype(int) >= min_id].head(380)
        max_id = df_jogosCamp["ID"].astype(int).max()

    elif year == 2021:
        df_brasFul["data"] = pd.to_datetime(df_brasFul["data"], format="%d/%m/%Y")
        df_year = df_brasFul[df_brasFul["data"].dt.year == year]
        df_jogosCamp = df_year[df_year["data"] > pd.to_datetime("28/5/2021")]
        min_id = df_jogosCamp["ID"].astype(int).min()
        max_id = df_jogosCamp["ID"].astype(int).max()

    else:
        # Filtra linhas com o ano do campeonato
        df_brasFul["data"] = pd.to_datetime(df_brasFul["data"], format="%d/%m/%Y")
        df_jogosCamp = df_brasFul[df_brasFul["data"].dt.year == year]
        min_id = df_jogosCamp["ID"].astype(int).min()
        max_id = df_jogosCamp["ID"].astype(int).max()

    return max_id,min_id

max_id, min_id = localId(df_brasFul,year)


filtered_df = df_brasGols[(df_brasGols['partida_id'] >= (min_id)) & (df_brasGols['partida_id'] <= (max_id))]

# Criar um dicionário para armazenar a contagem de jogadores
jogadores_contagem = {}

# Iterar pelas linhas do DataFrame filtrado
for index, row in filtered_df.iterrows():
    atleta = row['atleta']

    if pd.notnull(atleta):
        if atleta in jogadores_contagem:
            jogadores_contagem[atleta] += 1
        else:
            jogadores_contagem[atleta] = 1

jogadores_contagem_ordenada = dict(
    sorted(jogadores_contagem.items(), key=lambda item: item[1], reverse=True))

# Criar um DataFrame a partir do dicionário ordenado
df_contagem_ordenada = pd.DataFrame(
    jogadores_contagem_ordenada.items(), columns=[  'Atleta', 'Gols'])


#################  Contagem de cartões por ano #################
filtered_df = df_brasCards[(df_brasCards['partida_id'] >= (
    min_id)) & (df_brasCards['partida_id'] <= (max_id))]

# Criar um dicionário para armazenar a contagem de jogadores
jogadores_contagem = {}

# Iterar pelas linhas do DataFrame filtrado
for index, row in filtered_df.iterrows():
    atleta = row['atleta']

    if pd.notnull(atleta):
        if atleta in jogadores_contagem:
            jogadores_contagem[atleta] += 1
        else:
            jogadores_contagem[atleta] = 1

jogadores_contagem_ordenada = dict(
    sorted(jogadores_contagem.items(), key=lambda item: item[1], reverse=True))

# Criar um DataFrame a partir do dicionário ordenado
df_contagem_Card_ordenada = pd.DataFrame(
    jogadores_contagem_ordenada.items(), columns=['Atleta', 'Cartoes'])

 ######## GOLS MARCADOS e GOLS SOFRIDOS ################
def create_data_gols(df_data, club, year):
    df_clubMan = df_data[
        (df_data["time_man"] == club) &
        (df_data["ano_campeonato"] == year)
    ]
    # Calculando o total de gols marcados pelo mandante
    gols_man = df_clubMan['gols_man'].sum()
    gols_do_vis = df_clubMan['gols_vis'].sum()

    # Filtrando os dados para o clube  como visitante e no ano específico
    df_clubVis = df_data[
        (df_data["time_vis"] == club) &
        (df_data["ano_campeonato"] == year)
    ]

    # Calculando o total de gols marcados pelo clube como visitante
    gols_vis = df_clubVis['gols_vis'].sum()
    gols_do_man = df_clubVis['gols_man'].sum()

    # Calculando o total de jogos em que o clube marcou gols como mandante e visitante
    total_gols = int(gols_man + gols_vis)
    total_gols_sofridos = int(gols_do_man + gols_do_vis)
    saldo =int( total_gols - total_gols_sofridos)

    # Criar DF com os dados e ordenar por rodada
    df_pos = df_data[df_data["ano_campeonato"] == year]
    df_pos = df_pos[(df_pos["time_man"] == club) |
                    (df_pos["time_vis"] == club)]
    df_pos = df_pos.sort_values(by='rodada')

    return total_gols, total_gols_sofridos, saldo



##### Criar tabela final do campeonato ###########

def create_create_table(df_data, year):
    # Cria um DataFrame vazio com as colunas desejadas
    df_table_games = pd.DataFrame(columns=[
                                  "Clube", "Pontos", "Vitórias", "Empates", "Derrotas", "Gols Marcados", "Gols Sofridos", "Saldo"])

    # Seleciona os clubes que jogaram como mandante no ano especificado, filtra e ordena em ordem alfabética
    clubs = sorted(df_data[df_data["ano_campeonato"]== year]["time_man"].unique())

    for club in clubs:
      
        df_clubMan = df_data[
        (df_data["time_man"] == club) &
        (df_data["ano_campeonato"] == year)
        ]
        df_clubVis = df_data[
            (df_data["time_vis"] == club) &
            (df_data["ano_campeonato"] == year)
        ]
        vic_man = len(df_clubMan[df_clubMan["gols_man"] > df_clubMan["gols_vis"]])
        vic_vis = len(df_clubVis[df_clubVis["gols_vis"] > df_clubVis["gols_man"]])
        victories = vic_man + vic_vis

        emp_man = len(df_clubMan[df_clubMan["gols_man"] == df_clubMan["gols_vis"]])
        emp_vis = len(df_clubVis[df_clubVis["gols_vis"] == df_clubVis["gols_man"]])
        empates = emp_man + emp_vis

        der_man = len(df_clubMan[df_clubMan["gols_man"] < df_clubMan["gols_vis"]])
        der_vis = len(df_clubVis[df_clubVis["gols_vis"] < df_clubVis["gols_man"]])
        derrotas = der_man + der_vis
        
        df_clubMan = df_data[
        (df_data["time_man"] == club) &
        (df_data["ano_campeonato"] == year)
        ]
        # Calculando o total de gols marcados pelo mandante
        gols_man = df_clubMan['gols_man'].sum()
        gols_do_vis = df_clubMan['gols_vis'].sum()

        # Filtrando os dados para o clube  como visitante e no ano específico
        df_clubVis = df_data[
            (df_data["time_vis"] == club) &
            (df_data["ano_campeonato"] == year)
        ]

        # Calculando o total de gols marcados pelo clube como visitante
        gols_vis = df_clubVis['gols_vis'].sum()
        gols_do_man = df_clubVis['gols_man'].sum()

        # Calculando o total de jogos em que o clube marcou gols como mandante e visitante
        total_gols = int(gols_man + gols_vis)
        total_gols_sofridos = int(gols_do_man + gols_do_vis)
        saldo =int( total_gols - total_gols_sofridos)

        # Criar DF com os dados e ordenar por rodada
        df_pos = df_data[df_data["ano_campeonato"] == year]
        df_pos = df_pos[(df_pos["time_man"] == club) |
                        (df_pos["time_vis"] == club)]
        df_pos = df_pos.sort_values(by='rodada')
       
        pontos = (victories * 3) + empates  # Calcula os pontos corretamente
        new_Header = {"Clube": club, "Pontos": pontos, "Vitórias": victories, "Empates": empates, "Derrotas": derrotas, "Gols Marcados": total_gols,
                    "Gols Sofridos": total_gols_sofridos, "Saldo": saldo}
        df_table_games = pd.concat([df_table_games, pd.DataFrame([new_Header])], ignore_index=True)
    # Ordena o DataFrame por pontos de forma decrescente
    df_table_games = df_table_games.sort_values(by=["Pontos", "Vitórias", "Saldo"], ascending=[False, False, False])
    # Adiciona a coluna de sequência numérica
    df_table_games.insert(0, "Posição", range(1, len(df_table_games) + 1))

    return df_table_games

resulting_table_games = create_create_table(df_data, year)

first = resulting_table_games.iloc[0]["Clube"]
second = resulting_table_games.iloc[1]["Clube"]

last_4_clubs = resulting_table_games.tail(4)

# Extract the "Clube" column values for the last 4 clubs
rebaixados = last_4_clubs["Clube"].tolist()

# Colorir data frame
def highlight_rows(s):
    styles = []
    for i in range(len(s)):
        if i < 6:
            styles.append('background-color: rgba(93, 178, 48, 0.3);')
        elif i >= len(s) - 4:
            styles.append('background-color: rgba(243, 9, 9, 0.3)')
        else:
            styles.append('')
    return styles

styled_resulting_table_games = resulting_table_games.style.apply(highlight_rows)

########## FRONT END ##################
with st.container():
    st.markdown("<h4 style='text-align: center;'>Dados Gerais do campeonato</h4><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success(f"**Campeão:** {first} ")
    with col2:
        st.info(f"**Vice-Campeão:** {second} ")

    st.error(f"**Rebaixados:** {', '.join(rebaixados)}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Vitória dos Mandantes:** {vic_man} ")
    with col2:
        st.write(f"**Vitória dos Visitantes:** {vic_vis} ")
    with col3:
        st.write(f"**Total de Empates:** {empat} ")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Total de Gols Marcados:** {gols_marc} ") 
    with col2:
        st.write(f"**Gols Mandantes:** {gols_man} ")
    with col3:
        st.write(f"**Gols Visitantes:** {gols_vis} ")

st.divider()

try:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Artilheiros do campeonato**")
        st.dataframe(df_contagem_ordenada,
                     column_config={"Gols": st.column_config.ProgressColumn(
                         "Gols marcados",
                         help="Número de Gols marcados por jogador",
                         format="%d",
                         min_value=0,
                         max_value=int(df_contagem_ordenada['Gols'].max())
                     ),
                     }, height=300, width=400,
                     hide_index=True)

######### Tabela de cartões recebidos #######
    with col2:
        st.markdown(f"**Cartões** ")
        st.dataframe(df_contagem_Card_ordenada,
                     column_config={"Cartoes": st.column_config.ProgressColumn(
                         "Cartões Recebidos",
                         help="Número de cartões recebidos por jogador",
                         format="%d",
                         min_value=0,
                         max_value=int(
                             df_contagem_Card_ordenada['Cartoes'].max())
                     ),
                     }, height=300, width=400,
                     hide_index=True)
except:
    st.write("❗❗❗❗❗❗❗ Dados disponíveis apenas entre os anos de 2014-2022 ❗❗❗❗❗❗❗")

st.divider()

st.markdown("<h4 style='text-align: center;'>Tabela Final do Campeonato</h4>", unsafe_allow_html=True)

try:
    st.dataframe(styled_resulting_table_games,
                column_config={"Pontos": st.column_config.ProgressColumn(
                    "Progresso Campeonato",
                    help="Progresso Campeonato brasileiro",
                    format="%d",
                    min_value=0,
                    max_value=int(resulting_table_games['Pontos'].max())
                ),
                }, height=740, width=900,
                hide_index=True)
except:
    st.write("❗❗❗❗❗❗❗  Dados ainda não disponíveis  ❗❗❗❗❗❗")
