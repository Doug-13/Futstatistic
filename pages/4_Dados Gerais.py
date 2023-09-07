import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


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



st.sidebar.title("Dados Gerais")
st.sidebar.markdown("Ainda nesta página!")
st.sidebar.write("- Ranking Brasileiro!")
st.sidebar.write("- Ranking artilheiros!")
st.sidebar.write("- Ranking Cartões!")
st.sidebar.markdown("<h1 style='text-align: center;'></h1><br><br>", unsafe_allow_html=True)

st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")
# st.sidebar.markdown('''
# # Atalhos
# - [Início da Página](#section-1)
# - [Ranking do Brasileirão](#section-2)
# - [Artilheiros do Campeonato entre 2014 e 20222](#section-3)
# ''', unsafe_allow_html=True)



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


st.markdown("<h3 style='text-align: center;'>5 Primeiros colocados de todos os campeonatos</h3>", unsafe_allow_html=True)


# Caixa de seleção para escolher o clube
selected_club = st.selectbox("Selecione um clube para destacá-lo na tabela:", all_clubs)

# Definir um DataFrame estilizado com formatação condicional
styled_df = df_table_positions.style.applymap(lambda club: highlight_club(club, selected_club), subset=df_table_positions.columns[1:])

# Exibir o DataFrame estilizado no Streamlit

def get_club_logo(club_man):
    logo_mapping = {
        'América-MG': "https://logodetimes.com/times/america-mineiro/logo-america-mineiro-256.png",
        "America-MG":"https://logodetimes.com/times/america-mineiro/logo-america-mineiro-256.png",
        'América-RN': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AmericaFC-RN.svg/180px-AmericaFC-RN.svg.png",
        'Athletico-PR': "https://logodetimes.com/times/atletico-paranaense/logo-atletico-paranaense-256.png",
        'Atlético-PR': "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CA_Paranaense.svg/250px-CA_Paranaense.svg.png",
        'Athletico-PR':"https://logodetimes.com/times/atletico-paranaense/logo-atletico-paranaense-256.png",
        'Atletico-PR':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CA_Paranaense.svg/250px-CA_Paranaense.svg.png", 
        'Atlético-GO': "https://logodetimes.com/times/atletico-goianiense/logo-atletico-goianiense-com-estrela-256.png",
        "Atletico-GO":"https://logodetimes.com/times/atletico-goianiense/logo-atletico-goianiense-com-estrela-256.png",
        "Atletico-MG":"https://logodetimes.com/times/atletico-mineiro/logo-atletico-mineiro-256.png",
        'Atlético-MG': "https://logodetimes.com/times/atletico-mineiro/logo-atletico-mineiro-256.png",
        'Avaí FC': "https://logodetimes.com/times/avai/logo-avai-256.png",
        "Avai":"https://logodetimes.com/times/avai/logo-avai-256.png",
        'Barueri': "https://upload.wikimedia.org/wikipedia/pt/thumb/a/af/Gr%C3%AAmio_Barueri.png/120px-Gr%C3%AAmio_Barueri.png",
        'Botafogo': "https://logodetimes.com/times/botafogo/logo-botafogo-256.png",
        "Botafogo-RJ": "https://logodetimes.com/times/botafogo/logo-botafogo-256.png",
        'Brasiliense-DF': "https://seeklogo.com/images/B/Brasiliense_Futebol_Clube-DF-logo-24AEB16A54-seeklogo.com.png",
        'Brasiliense': "https://seeklogo.com/images/B/Brasiliense_Futebol_Clube-DF-logo-24AEB16A54-seeklogo.com.png",
        'CSA': "https://logodetimes.com/times/csa/logo-csa-256.png",
        'Ceará SC': "https://logodetimes.com/times/ceara/logo-ceara-256.png",
        "Ceara": "https://logodetimes.com/times/ceara/logo-ceara-256.png",
        'Chapecoense': "https://logodetimes.com/times/chapecoense/logo-chapecoense-256.png",
        'Corinthians': "https://logodetimes.com/times/corinthians/logo-corinthians-256.png",
        "Coritiba": "https://logodetimes.com/times/coritiba/logo-coritiba-256.png",       
        'Coritiba FC': "https://logodetimes.com/times/coritiba/logo-coritiba-256.png",
        'Criciúma EC': "https://logodetimes.com/times/criciuma/logo-criciuma-5.png",
        'Criciuma': "https://logodetimes.com/times/criciuma/logo-criciuma-5.png",
        'Cruzeiro': "https://logodetimes.com/times/cruzeiro/logo-cruzeiro-256.png",
        'Cuiabá-MT': "https://logodetimes.com/times/cuiaba/logo-cuiaba-256.png",
        "Cuiaba": "https://logodetimes.com/times/cuiaba/logo-cuiaba-256.png", 
        "EC Bahia": "https://logodetimes.com/times/bahia/logo-bahia-256.png",
        "Bahia": "https://logodetimes.com/times/bahia/logo-bahia-256.png",
        "Vitoria": "https://logodetimes.com/times/vitoria/logo-vitoria-256.png",       
        'EC Vitória': "https://logodetimes.com/times/vitoria/logo-vitoria-256.png",
        'Figueirense FC': "https://logodetimes.com/times/figueirense/logo-figueirense-256.png",
        "Figueirense":"https://logodetimes.com/times/figueirense/logo-figueirense-256.png",    
        'Flamengo': "https://logodetimes.com/times/flamengo/logo-flamengo-256.png",
        'Fluminense': "https://logodetimes.com/times/fluminense/logo-fluminense-256.png",
        'Fortaleza': "https://logodetimes.com/times/fortaleza/logo-fortaleza-256.png",
        'Goiás': "https://logodetimes.com/times/goias/logo-goias-esporte-clube-4096.png",
        'Goiás EC': "https://logodetimes.com/times/goias/logo-goias-esporte-clube-4096.png",
        'Goias': "https://logodetimes.com/times/goias/logo-goias-esporte-clube-4096.png",  
        'Grêmio': "https://logodetimes.com/times/gremio/logo-gremio-256.png",
        'Gremio': "https://logodetimes.com/times/gremio/logo-gremio-256.png",
        'Guarani': "https://logodetimes.com/times/guarani/logo-guarani-256.png",
        'Internacional': "https://logodetimes.com/times/internacional/logo-internacional-256.png",
        'Ipatinga FC': "https://upload.wikimedia.org/wikipedia/pt/thumb/9/95/IpatingaFC.png/120px-IpatingaFC.png",
        'Joinville-SC': "https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Joinville_Esporte_Clube_logo.svg/150px-Joinville_Esporte_Clube_logo.svg.png",
        'Juventude': "https://logodetimes.com/times/juventude/logo-juventude-256.png",
        'Náutico': "https://logodetimes.com/times/nautico/logo-nautico-256.png",
        "Nautico": "https://logodetimes.com/times/nautico/logo-nautico-256.png",
        'Palmeiras': "https://logodetimes.com/times/palmeiras/logo-palmeiras-256.png",
        'Paraná': "https://logodetimes.com/times/parana/logo-parana-256.png",
        "Parana": "https://logodetimes.com/times/parana/logo-parana-256.png",
        "Paysandu":"https://logodetimes.com/times/paysandu/logo-paysandu-5.png",
        'Paysandu SC': "https://logodetimes.com/times/paysandu/logo-paysandu-5.png",
        "Paysandu": "https://logodetimes.com/times/paysandu/logo-paysandu-5.png",
        'Ponte Preta': "https://logodetimes.com/times/ponte-preta/logo-ponte-preta-256.png",
        'Portuguesa': "https://logodownload.org/wp-content/uploads/2019/09/portuguesa-sp-logo-5.png",
        'RB Bragantino': "https://logodetimes.com/times/red-bull-bragantino/logo-red-bull-bragantino-256.png",
        "Bragantino": "https://logodetimes.com/times/red-bull-bragantino/logo-red-bull-bragantino-256.png",
        'Santa Cruz': "https://logodetimes.com/times/santa-cruz/logo-santa-cruz-256.png",
        'Santo André': "https://logodetimes.com/times/santo-andre/logo-santo-andre-256.png",
        "Santo Andre":"https://logodetimes.com/times/santo-andre/logo-santo-andre-256.png",
        'Santos': "https://logodetimes.com/times/santos/logo-santos-256.png  ",
        'Santos FC': "https://logodetimes.com/times/santos/logo-santos-256.png  ",
        'Sport Recife': "https://upload.wikimedia.org/wikipedia/en/thumb/4/45/Sport_Club_Recife.svg/170px-Sport_Club_Recife.svg.png",
        "Sport":"https://upload.wikimedia.org/wikipedia/en/thumb/4/45/Sport_Club_Recife.svg/170px-Sport_Club_Recife.svg.png",
        'São Caetano': "https://logodetimes.com/times/sao-caetano/logo-sao-caetano-256.png",
        "Sao Caetano":"https://logodetimes.com/times/sao-caetano/logo-sao-caetano-256.png",
        'São Paulo': "https://logodetimes.com/times/sao-paulo/logo-sao-paulo-256.png",
        'Sao Paulo':"https://logodetimes.com/times/sao-paulo/logo-sao-paulo-256.png",
        'Vasco da Gama': "https://logodetimes.com/times/vasco-da-gama/logo-vasco-da-gama-256.png",
        'Vasco': "https://logodetimes.com/times/vasco-da-gama/logo-vasco-da-gama-256.png",
    }
    return logo_mapping.get(club_man, "")


# Função para destacar o clube selecionado
def highlight_club(club, selected_club):
    if club == selected_club:
        return "background-color: rgb(174, 173, 72); color: rgb(39, 39, 43);"
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



######   Front   #########

st.dataframe(resultado_df, height=30, width=900, hide_index=True)

st.dataframe(styled_df, height=740, width=900, hide_index=True)


def df_table_games(df_data):    
    # Lista para armazenar os dados de cada clube
    club_data_list = []

    # Agrupa os dados pelo clube mandante
    club_man_data = df_data.groupby("time_man")

    # Agrupa os dados pelo clube visitante
    club_vis_data = df_data.groupby("time_vis")

    # Encontra todos os clubes únicos
    clubs = set(df_data["time_man"].unique()) | set(df_data["time_vis"].unique())

    for club in clubs:
        # Obtém os dados para o clube mandante
        club_man_matches = club_man_data.get_group(club) if club in club_man_data.groups else pd.DataFrame()

        # Obtém os dados para o clube visitante
        club_vis_matches = club_vis_data.get_group(club) if club in club_vis_data.groups else pd.DataFrame()

        # Calcula as estatísticas
        victories = len(club_man_matches[club_man_matches["gols_man"] > club_man_matches["gols_vis"]]) + len(club_vis_matches[club_vis_matches["gols_vis"] > club_vis_matches["gols_man"]])
        empates = len(club_man_matches[club_man_matches["gols_man"] == club_man_matches["gols_vis"]]) + len(club_vis_matches[club_vis_matches["gols_vis"] == club_vis_matches["gols_man"]])
        derrotas = len(club_man_matches[club_man_matches["gols_man"] < club_man_matches["gols_vis"]]) + len(club_vis_matches[club_vis_matches["gols_vis"] < club_vis_matches["gols_man"]])
        
        total_gols_man = club_man_matches["gols_man"].sum() + club_vis_matches["gols_vis"].sum()
        total_gols_vis = club_man_matches["gols_vis"].sum() + club_vis_matches["gols_man"].sum()
       
        saldo = total_gols_man - total_gols_vis
        
        pontos = (victories * 3) + empates  # Calcula os pontos
        
        aprov = round((pontos * 100) / ((victories + empates + derrotas) * 3), 2)

        # Aplica a função get_club_logo para obter o logotipo do clube
        logo_man = df_data[df_data["time_man"] == club]["time_man"].apply(get_club_logo).values[0]

        # Adiciona os dados à lista
        club_data_list.append({"Escudo": logo_man, "Clube": club, "Pontos": pontos, "Vitórias": victories, "Empates": empates, "Derrotas": derrotas, "Gols Marc.": str(int(total_gols_man)),
                                                "Gols Sof.": str(int(total_gols_vis)), "Saldo": saldo,"Aproveit.%":aprov})

    # Cria o DataFrame a partir da lista de dicionários
    df_table_games = pd.DataFrame(club_data_list)

    # Ordena o DataFrame por pontos de forma decrescente
    df_table_games = df_table_games.sort_values(by=["Pontos", "Vitórias", "Saldo"], ascending=[False, False, False])
    # Adiciona a coluna de sequência numérica
    df_table_games.insert(0, "Pos", range(1, len(df_table_games) + 1))

    return df_table_games

# Chama a função para criar a tabela
resulting_table_games = df_table_games(df_data)
# st.header("Ranking do Brasileirão")

st.markdown("<h3 style='text-align: center;'>Ranking brasileirão</h3>", unsafe_allow_html=True)


st.dataframe(resulting_table_games, height=800, width=800, hide_index=True, 
             column_config={
                 "Escudo": st.column_config.ImageColumn(),
                 "Pontos": st.column_config.ProgressColumn(
                     "Pontos",
                     help="Total de Pontos em todos os campeonatos",
                     format="%d",
                     min_value=0,
                     max_value=int(resulting_table_games['Pontos'].max())
                 ),
             })

#################  Contagem de gols por ano #################

jogadores_contagem = {}

# Iterar pelas linhas do DataFrame filtrado
for index, row in df_brasGols.iterrows():
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
    jogadores_contagem_ordenada.items(), columns=['Atleta', 'Gols'])



#################  Contagem de cartões por ano #################

jogadores_contagem = {}

# Iterar pelas linhas do DataFrame filtrado
for index, row in df_brasCards.iterrows():
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



col1, col2 = st.columns(2)
with col1:
    st.markdown("**Ranking Artilheiros**")
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

with col2:
        st.markdown(f"**Ranking Cartões** ")
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