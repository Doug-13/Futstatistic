import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# Importar funções
# from ..utilitarios.funct import get_club_logo
# from ..utilitarios.funct import get_club_color

st.set_page_config(
    page_title="Estatísticas",
    # page_icon = "",
    layout="wide"
)

df_data = st.session_state["data"]
df_brasGols = st.session_state["dataBrasGols"]
df_brasFul = st.session_state["dataBrasFull"]
df_brasCards = st.session_state["dataBrasCards"] 


# Criar caixa de seleção de Ano
years = sorted(df_data["ano_campeonato"].value_counts().index, reverse=True)
year = st.sidebar.selectbox("Ano", years)

# Criar caixa de seleção de Clubes
clubs = df_data[df_data["ano_campeonato"] == year]
clubs = sorted(clubs["time_man"].value_counts().index)
club = st.sidebar.selectbox("Time", clubs)

################## Buscar escudo do clube ##################
def get_club_logo(club):
    logo_mapping = {
    'América-MG': "https://logodetimes.com/times/america-mineiro/logo-america-mineiro-256.png",
    'América-RN': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/AmericaFC-RN.svg/180px-AmericaFC-RN.svg.png",
    'Athletico-PR':"https://logodetimes.com/times/atletico-paranaense/logo-atletico-paranaense-256.png",
    'Atlético-PR':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CA_Paranaense.svg/250px-CA_Paranaense.svg.png",
    'Atlético-GO': "https://logodetimes.com/times/atletico-goianiense/logo-atletico-goianiense-com-estrela-256.png",
    'Atlético-MG':"https://logodetimes.com/times/atletico-mineiro/logo-atletico-mineiro-256.png",
    'Avaí FC':"https://logodetimes.com/times/avai/logo-avai-256.png",
    'Barueri':"https://upload.wikimedia.org/wikipedia/pt/thumb/a/af/Gr%C3%AAmio_Barueri.png/120px-Gr%C3%AAmio_Barueri.png",
    'Botafogo':"https://logodetimes.com/times/botafogo/logo-botafogo-256.png",
    'Brasiliense-DF':"https://upload.wikimedia.org/wikipedia/pt/thumb/3/3a/Brasiliense_Futebol_Clube.png/120px-Brasiliense_Futebol_Clube.png",
    'CSA': "https://logodetimes.com/times/csa/logo-csa-256.png",
    'Ceará SC':"https://logodetimes.com/times/ceara/logo-ceara-256.png",
    'Chapecoense': "https://logodetimes.com/times/chapecoense/logo-chapecoense-256.png",
    'Corinthians': "https://logodetimes.com/times/corinthians/logo-corinthians-256.png",
    'Coritiba FC':"https://logodetimes.com/times/coritiba/logo-coritiba-256.png",
    'Criciúma EC':"https://logodetimes.com/times/criciuma/logo-criciuma-5.png",
    'Cruzeiro':"https://logodetimes.com/times/cruzeiro/logo-cruzeiro-256.png",
    'Cuiabá-MT':"https://logodetimes.com/times/cuiaba/logo-cuiaba-256.png",
    "EC Bahia":"https://logodetimes.com/times/bahia/logo-bahia-256.png",
    'EC Vitória':"https://logodetimes.com/times/vitoria/logo-vitoria-256.png",
    'Figueirense FC': "https://logodetimes.com/times/figueirense/logo-figueirense-256.png",
    'Flamengo': "https://logodetimes.com/times/flamengo/logo-flamengo-256.png",
    'Fluminense':"https://logodetimes.com/times/fluminense/logo-fluminense-256.png",
    'Fortaleza': "https://logodetimes.com/times/fortaleza/logo-fortaleza-256.png",
    'Goiás' or 'Goiás EC':"https://logodetimes.com/times/goias/logo-goias-esporte-clube-4096.png",
    'Grêmio': "https://logodetimes.com/times/gremio/logo-gremio-256.png",
    'Guarani': "https://logodetimes.com/times/guarani/logo-guarani-256.png",
    'Internacional':"https://logodetimes.com/times/internacional/logo-internacional-256.png",
    'Ipatinga FC': "https://upload.wikimedia.org/wikipedia/pt/thumb/9/95/IpatingaFC.png/120px-IpatingaFC.png",
    'Joinville-SC':"https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Joinville_Esporte_Clube_logo.svg/150px-Joinville_Esporte_Clube_logo.svg.png",
    'Juventude':"https://logodetimes.com/times/juventude/logo-juventude-256.png",
    'Náutico':"https://logodetimes.com/times/nautico/logo-nautico-256.png",
    'Palmeiras':"https://logodetimes.com/times/palmeiras/logo-palmeiras-256.png",
    'Paraná':"https://logodetimes.com/times/parana/logo-parana-256.png",
    'Paysandu SC':"https://logodetimes.com/times/paysandu/logo-paysandu-5.png",
    'Ponte Preta':"https://logodetimes.com/times/ponte-preta/logo-ponte-preta-256.png",
    'Portuguesa':"https://logodetimes.com/times/portugal/selecao-portuguesa-de-futebol-4096.png",
    'RB Bragantino': "https://logodetimes.com/times/red-bull-bragantino/logo-red-bull-bragantino-256.png",
    'Santa Cruz': "https://logodetimes.com/times/santa-cruz/logo-santa-cruz-256.png",
    'Santo André': "https://logodetimes.com/times/santo-andre/logo-santo-andre-256.png",
    'Santos' or 'Santos FC': "https://logodetimes.com/times/santos/logo-santos-256.png  ",
    'Sport Recife':"https://upload.wikimedia.org/wikipedia/en/thumb/4/45/Sport_Club_Recife.svg/170px-Sport_Club_Recife.svg.png",
    'São Caetano':"https://logodetimes.com/times/sao-caetano/logo-sao-caetano-256.png",
    'São Paulo': "https://logodetimes.com/times/sao-paulo/logo-sao-paulo-256.png",
    'Vasco da Gama':"https://logodetimes.com/times/vasco-da-gama/logo-vasco-da-gama-256.png",
}
    return logo_mapping.get(club, "")
################## alterar nomes para pesquisas nos dados do Kaggle ##################
def get_club_name(club):
    club_mapping = {
    'América-MG': "America-MG",
    'Atlético-PR':"Athletico-PR",
    'Atlético-GO': "Atletico-GO",
    'Atlético-MG':"Atletico-MG",
    'Avaí FC':"Avai",
    'Botafogo':"Botafogo-RJ",
    'Ceará SC':"Ceara",
    'Coritiba FC':"Coritiba",    
    'Cuiabá-MT':"Cuiaba",
    "EC Bahia":"Bahia",
    'EC Vitória':"Vitoria",
    'Figueirense FC': "Figueirense",
    'Goiás' or 'Goiás EC': 'Goias',
    'Grêmio':'Gremio',    
    'Náutico':"Nautico",
    'Paraná':"Parana",
    'Paysandu SC':"Paysandu",
    'RB Bragantino': "Bragantino",
    'Santo André': "Santo Andre",
    'Santos' or 'Santos FC': 'Santos',
    'Sport Recife':"Sport",
    'São Caetano': "Sao Caetano",
    'São Paulo': 'Sao Paulo',
}
    return club_mapping .get(club, club)
################## Definir cor para gráfico ############################  
def get_club_color(club):
    color_mapping = {
        'América-MG'or 'Chapecoense' or 'Coritiba FC'or 'Cuiabá-MT'or 'Fluminense' or 'Goiás'or 'Goiás EC'or 'Guarani'or 'Juventude'or 'Palmeiras': "green",
        'América-RN' or 'Athletico-PR' or 'Atlético-GO'or 'Atlético-PR'or 'EC Vitória' or 'Flamengo'or 'Internacional'or 'Joinville-SC'or 'Náutico'or 'Paraná'or 'Portuguesa'or 'RB Bragantino' or 'Santa Cruz' or 'Sport Recife'  or 'São Paulo':"red",
        'Atlético-MG' or 'Botafogo'or 'Ceará SC' or 'Figueirense FC' or 'Corinthians'or 'Ponte Preta'or 'Santos'or 'Santos FC'or 'Vasco da Gama':"black",
        'Avaí FC' or 'Barueri' or 'CSA'or 'Cruzeiro'or 'EC Bahia'or 'CSA' or 'Fortaleza'or 'Grêmio'or 'Ipatinga FC'or 'Paysandu SC'or 'São Caetano':"blue",
        'Brasiliense-DF'or 'Criciúma EC':"yellow"
}
    return color_mapping.get(club, "black")

def create_match_table(df_data, year, club):
    df_pos = df_data[(df_data["ano_campeonato"] == year) & ((df_data["time_man"] == club) | (df_data["time_vis"] == club))]
    df_pos = df_pos.sort_values(by='rodada')
    columns = ["data", "rodada", "publico", "time_man", "time_vis"]
    df_pos['data'] = pd.to_datetime(df_pos['data'])
   
    df_tabela = df_pos[columns]
    df_tabela["Placar"] = df_pos["time_man"] + " " + df_pos["gols_man"].astype(str) + " x " + df_pos["gols_vis"].astype(str) + " " + df_pos["time_vis"]
    df_tabela["data"] = df_tabela["data"].dt.strftime('%d/%m/%y')
    # Add new columns for the logo URLs using the get_club_logo function
    df_tabela["Logo_man"] = df_tabela["time_man"].apply(get_club_logo)
    df_tabela["Logo_vis"] = df_tabela["time_vis"].apply(get_club_logo)

    # Select and rename columns for the final table
    df_tab = df_tabela[["data", "rodada", "Logo_man", "Placar", "Logo_vis", "publico"]]
    df_tab.rename(columns={"data": "Data do Jogo", "rodada": "Rodada", "Logo_man": "Escudo Mandante", "Logo_vis": "Escudo Visitante", "publico": "Público"}, inplace=True)

    return df_tab
    


logo = get_club_logo(club)
color = get_club_color(club)
clubGols = get_club_name(club)
table = create_match_table(df_data, year, club)


# Calcular número de rodadas do campeonato
df_year = df_data[df_data["ano_campeonato"] == year]
ultRod = df_year["rodada"].max()

# Ver posição do clube ao fim do campeonato
club_location_man = df_year[(df_year["rodada"] == ultRod) & (df_year["time_man"] == club)]["colocacao_man"]

# Filtrar para o clube como time visitante na última rodada
club_location_vis = df_year[(df_year["rodada"] == ultRod) & (df_year["time_vis"] == club)]["colocacao_vis"]

# Verificar se o clube estava como time mandante ou visitante e obter a colocação correspondente
if not club_location_man.empty:
    club_location = club_location_man.values[0]
elif not club_location_vis.empty:
    club_location = club_location_vis.values[0]
else:
    club_location = "N/A"


######## Calcular vitórias, derrotas e empates ########
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

######## GOLS MARCADOS e GOLS SOFRIDOS ################
df_clubMan = df_data[
    (df_data["time_man"] == club) &
    (df_data["ano_campeonato"] == year)
]

# Calculando o total de gols marcados pelo mandante
gols_man = df_clubMan['gols_man'].sum()
gols_do_vis= df_clubMan['gols_vis'].sum()

# Filtrando os dados para o clube  como visitante e no ano específico
df_clubVis = df_data[
    (df_data["time_vis"] == club) &
    (df_data["ano_campeonato"] == year)
]

# Calculando o total de gols marcados pelo clube como visitante
gols_vis = df_clubVis['gols_vis'].sum()
gols_do_man = df_clubVis['gols_man'].sum()

# Calculando o total de jogos em que o clube marcou gols como mandante e visitante
total_gols = gols_man + gols_vis
total_gols_sofridos = gols_do_man + gols_do_vis
saldo = total_gols - total_gols_sofridos 


###   Criar DF com os dados e ordenar por rodada
df_pos = df_data[df_data["ano_campeonato"] == year]
df_pos = df_pos[(df_pos["time_man"] == club) | (df_pos["time_vis"] == club)]
df_pos = df_pos.sort_values(by='rodada')
# df_pos

#################  Selecionar campeonatos por ano #################

### filtro especial para campeonatos de 2020 e 2021 que foram situações especiais devido a COVID  ###

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

#################  Contagem de gols por ano ################# 

filtered_df = df_brasGols[(df_brasGols['partida_id'] >= (min_id)) & (df_brasGols['partida_id'] <= (max_id))]
filtered_df = filtered_df[(df_brasGols['clube'])==clubGols]

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

jogadores_contagem_ordenada = dict(sorted(jogadores_contagem.items(), key=lambda item: item[1], reverse=True))

# Criar um DataFrame a partir do dicionário ordenado
df_contagem_ordenada = pd.DataFrame(jogadores_contagem_ordenada.items(), columns=['Atleta', 'Gols'])

# Imprimir a tabela
# print(df_contagem_ordenada)

#################  Contagem de cartões por ano ################# 
filtered_df = df_brasCards[(df_brasCards['partida_id'] >= (min_id)) & (df_brasCards['partida_id'] <= (max_id))]
filtered_df = filtered_df[(df_brasCards['clube'])==clubGols]

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

jogadores_contagem_ordenada = dict(sorted(jogadores_contagem.items(), key=lambda item: item[1], reverse=True))

# Criar um DataFrame a partir do dicionário ordenado
df_contagem_Card_ordenada = pd.DataFrame(jogadores_contagem_ordenada.items(), columns=['Atleta', 'Cartoes'])


####################### Criar gráfico   #######################

df_posRod = df_data[(df_data["time_man"] == club) & (df_data["ano_campeonato"] == year)]
df_posVis = df_data[(df_data["time_vis"] == club) & (df_data["ano_campeonato"] == year)]

df_new = pd.concat([
    df_posRod[['rodada', 'colocacao_man']].rename(columns={'colocacao_man': 'posicao'}),
    df_posVis[['rodada', 'colocacao_vis']].rename(columns={'colocacao_vis': 'posicao'})
])

df_new = df_new.sort_values('rodada').reset_index(drop=True)
df_newTest = df_new['posicao']

# Plotar gráfico de linha
plt.figure(figsize=(8, 3))  # Definir o tamanho da figura
plt.plot(df_new['rodada'], df_new['posicao'], marker='', color=(f'{color}'), lw=0.5)
plt.xlabel('Rodada')
plt.ylabel('Posicao')
plt.title(f'Evolução do {club} no Brasileiro {year}')
plt.axhline(y=1, color='green', linestyle='-', lw=0.8)
plt.axhline(y=20, color='black', linestyle='-', lw=0.5)
plt.axhline(y=17, color='red', linestyle='--', lw=0.5, label="Zona de Rebaixamento")
plt.legend(loc='lower right')

# Ajustar eixo Y do maior para o menor
plt.ylim(22, 0)

# Inserir rótulo de dados
for index, row in df_new.iterrows():
    plt.text(row['rodada'], row['posicao'], str(row['posicao']), ha='center', va='bottom', fontsize=6)
#Remover bordas do gráfico
plt.axis('off')
plt.grid(True)
# plt.show()

####################### FRONT  ##############

# formatação do cabeçalho da página Logo + nome do clube
col1, col2,col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.title(f"{club}")

col1, col2,col3 = st.columns(3)
with col1:
    st.write(f"**Posição Final:** {club_location}")
with col2:
    st.markdown(f"**Brasileirão** {year}")



# Colunas de vitórias, Empates e derrotas
col1, col2,col3 = st.columns(3)
with col1:  
       st.markdown(f"**Vitórias:** {victories}")  
with col2:
       st.markdown(f"**Empates:** {empates}")
with col3:
       st.markdown(f'**Derrotas:** {derrotas}')

# Colunas de Gols marcados, Gols sofridos e Saldo
col1, col2,col3 = st.columns(3)
with col1:  
    st.markdown(f"**Gols marcados:** {total_gols}")     
with col2:
    st.markdown(f"**Gols sofridos:** {total_gols_sofridos}")
with col3:
    st.markdown(f'**Saldo:** {saldo}')

st.divider()

try:
    col1, col2 = st.columns(2)
    with col1:  
        st.write(f"**Artilheiros do clube**")     
        st.dataframe(df_contagem_ordenada,
                column_config={"Gols": st.column_config.ProgressColumn(
                                "Gols marcados",
                                help="Número de Gols marcados por jogador",
                                format="%d",
                                min_value=0,
                                max_value=  int(df_contagem_ordenada['Gols'].max())
            ),
        },height = 300, width = 400,
        hide_index=True  )
    with col2:
        st.markdown(f"**Cartões Amarelos** ") 
        st.dataframe(df_contagem_Card_ordenada,
                column_config={"Cartoes": st.column_config.ProgressColumn(
                                "Cartões Recebidos",
                                help="Número de cartões recebidos por jogador",
                                format="%d",
                                min_value=0,
                                max_value=  int(df_contagem_Card_ordenada['Cartoes'].max())
            ),
        },height = 300, width = 400,
        hide_index=True )
except:
    st.write("Dados disponíveis entre os anos de 2014-2022")

st.divider()

try:
    st.pyplot(plt)
except:
    st.write("Dados ainda não disponíveis")


st.dataframe(table,
                column_config={
                    "Escudo Mandante":st.column_config.ImageColumn(),
                    "Escudo Visitante":st.column_config.ImageColumn(),
        },height = 500, width = 800,
        hide_index=True)