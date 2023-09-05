import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

st.set_page_config(
    page_title="Estatísticas",
    page_icon = ":⚽:",
    layout="wide"
)
df_data = st.session_state["data"]
df_brasGols = st.session_state["dataBrasGols"]
df_brasFul = st.session_state["dataBrasFull"]
df_brasCards = st.session_state["dataBrasCards"]
df_brasPosition = st.session_state["df_brasPosition"]


# Criar caixa de seleção de Ano
logo = "https://upload.wikimedia.org/wikipedia/pt/thumb/4/42/Campeonato_Brasileiro_S%C3%A9rie_A_logo.png/109px-Campeonato_Brasileiro_S%C3%A9rie_A_logo.png?20160723160542"
col1, col2, col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.markdown("<h1 style='text-align: center;'>Campeonato Brasileiro</h1>", unsafe_allow_html=True)



# Funções para gerar tabelas de primeiros lugares por ano!
# year = 2003

# def create_create_table(df_data, year):
#     # Cria um DataFrame vazio com as colunas desejadas
#     df_table_games = pd.DataFrame(columns=[
#                                   "Clube", "Pontos", "Vitórias", "Empates", "Derrotas", "Gols Marcados", "Gols Sofridos", "Saldo"])

#     # Seleciona os clubes que jogaram como mandante no ano especificado, filtra e ordena em ordem alfabética
#     clubs = sorted(df_data[df_data["ano_campeonato"]== year]["time_man"].unique())

#     for club in clubs:
      
#         df_clubMan = df_data[
#         (df_data["time_man"] == club) &
#         (df_data["ano_campeonato"] == year)
#         ]
#         df_clubVis = df_data[
#             (df_data["time_vis"] == club) &
#             (df_data["ano_campeonato"] == year)
#         ]
#         vic_man = len(df_clubMan[df_clubMan["gols_man"] > df_clubMan["gols_vis"]])
#         vic_vis = len(df_clubVis[df_clubVis["gols_vis"] > df_clubVis["gols_man"]])
#         victories = vic_man + vic_vis

#         emp_man = len(df_clubMan[df_clubMan["gols_man"] == df_clubMan["gols_vis"]])
#         emp_vis = len(df_clubVis[df_clubVis["gols_vis"] == df_clubVis["gols_man"]])
#         empates = emp_man + emp_vis

#         der_man = len(df_clubMan[df_clubMan["gols_man"] < df_clubMan["gols_vis"]])
#         der_vis = len(df_clubVis[df_clubVis["gols_vis"] < df_clubVis["gols_man"]])
#         derrotas = der_man + der_vis
        
#         df_clubMan = df_data[
#         (df_data["time_man"] == club) &
#         (df_data["ano_campeonato"] == year)
#         ]
#         # Calculando o total de gols marcados pelo mandante
#         gols_man = df_clubMan['gols_man'].sum()
#         gols_do_vis = df_clubMan['gols_vis'].sum()

#         # Filtrando os dados para o clube  como visitante e no ano específico
#         df_clubVis = df_data[
#             (df_data["time_vis"] == club) &
#             (df_data["ano_campeonato"] == year)
#         ]

#         # Calculando o total de gols marcados pelo clube como visitante
#         gols_vis = df_clubVis['gols_vis'].sum()
#         gols_do_man = df_clubVis['gols_man'].sum()

#         # Calculando o total de jogos em que o clube marcou gols como mandante e visitante
#         total_gols = int(gols_man + gols_vis)
#         total_gols_sofridos = int(gols_do_man + gols_do_vis)
#         saldo =int( total_gols - total_gols_sofridos)

#         # Criar DF com os dados e ordenar por rodada
#         df_pos = df_data[df_data["ano_campeonato"] == year]
#         df_pos = df_pos[(df_pos["time_man"] == club) |
#                         (df_pos["time_vis"] == club)]
#         df_pos = df_pos.sort_values(by='rodada')
       
#         pontos = (victories * 3) + empates  # Calcula os pontos corretamente
#         new_Header = {"Clube": club, "Pontos": pontos, "Vitórias": victories, "Empates": empates, "Derrotas": derrotas, "Gols Marcados": total_gols,
#                     "Gols Sofridos": total_gols_sofridos, "Saldo": saldo}
#         df_table_games = pd.concat([df_table_games, pd.DataFrame([new_Header])], ignore_index=True)
#     # Ordena o DataFrame por pontos de forma decrescente
#     df_table_games = df_table_games.sort_values(by=["Pontos", "Vitórias", "Saldo"], ascending=[False, False, False])
#     # Adiciona a coluna de sequência numérica
#     df_table_games.insert(0, "Posição", range(1, len(df_table_games) + 1))

#     return df_table_games
# resulting_table_games = create_create_table(df_data, year)
# #Retornar apenas os 5 primeiros

# year = 2003

# def table_positions(df_data):
#     # Cria um DataFrame vazio para armazenar os resultados
#     df_table_games_geral = pd.DataFrame(columns=[
#         "Ano", "Campeão", "Vice-Campeão", "Terceiro lugar", "Quarto lugar", "Quinto Lugar"
#     ])

#     # Itera pelos anos de 2003 a 2023
#     for year in range(2003, 2023        ):
#         # Obtém a tabela de classificação para o ano atual
#         df_table = create_create_table(df_data, year)

#         # Obtém os 5 primeiros colocados
#         top_5 = df_table.head(5)

#         # Cria uma linha com os resultados para este ano
#         result_row = {
#             "Ano":str(int(year)),
#             "Campeão": top_5.iloc[0]["Clube"],
#             "Vice-Campeão": top_5.iloc[1]["Clube"],
#             "Terceiro lugar": top_5.iloc[2]["Clube"],
#             "Quarto lugar": top_5.iloc[3]["Clube"],
#             "Quinto Lugar": top_5.iloc[4]["Clube"]
#         }

#         # Adiciona a linha ao DataFrame de resultados
#         df_table_games_geral = df_table_games_geral.append(result_row, ignore_index=True)

#     return df_table_games_geral

# # Para obter a tabela de posições de 2003 a 2023
# resulting_table_games = table_positions(df_data)

# Criar dF com todos os clubes que ficaram entre os 5 primeiros

df = pd.DataFrame(df_brasPosition)

df_table_positions = df.copy()

# Obter todos os clubes únicos
all_clubs = sorted(pd.concat([
    df_table_positions['Campeão'],
    df_table_positions['Vice-Campeão'],
    df_table_positions['Terceiro Lugar'],
    df_table_positions['Quarto Lugar'],
    df_table_positions['Quinto-Lugar']
]).unique())

# Caixa de seleção para escolher o clube
selected_club = st.selectbox("Selecione um clube:", all_clubs)

# Definir um DataFrame estilizado com formatação condicional
styled_df = df_table_positions.style.applymap(lambda club: highlight_club(club, selected_club), subset=df_table_positions.columns[1:])

# Exibir o DataFrame estilizado no Streamlit

# Função para destacar o clube selecionado
def highlight_club(club, selected_club):
    if club == selected_club:
        return "background-color: rgb(238, 235, 56)"
    else:
        return ""

all_clubs = pd.concat([df_table_positions['Campeão'],df_table_positions['Vice-Campeão'], df_table_positions['Terceiro Lugar'], df_table_positions['Quarto Lugar'], df_table_positions['Quinto-Lugar']])

campeao_count = (df["Campeão"] == selected_club).sum()
vice_count = (df["Vice-Campeão"] == selected_club).sum()
terceiro_count = (df["Terceiro Lugar"] == selected_club).sum()
quarto_count = (df["Quarto Lugar"] == selected_club).sum()
quinto_count = (df["Quinto-Lugar"] == selected_club).sum()

# Criar um novo DataFrame com as contagens
contagem_df = pd.DataFrame({
    "Posição": ["Campeão", "Vice-Campeão", "Terceiro Lugar", "Quarto Lugar", "Quinto-Lugar"],
    "Contagem": [campeao_count, vice_count, terceiro_count, quarto_count, quinto_count]
})
resultado_df = contagem_df.T  # Transpor o DataFrame de contagem
resultado_df.columns = resultado_df.iloc[0]  # Usar a primeira linha como nomes das colunas
resultado_df = resultado_df[1:]


st.dataframe(resultado_df, height=30, width=900, hide_index=True)

st.dataframe(styled_df, height=740, width=900, hide_index=True)

# st.dataframe(clubs_positions, height=740, width=900, hide_index=True)

    


