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

st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")

logo = "https://upload.wikimedia.org/wikipedia/pt/thumb/4/42/Campeonato_Brasileiro_S%C3%A9rie_A_logo.png/109px-Campeonato_Brasileiro_S%C3%A9rie_A_logo.png?20160723160542"
col1, col2, col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.markdown("<h1 style='text-align: center;'>Campeonato Brasileiro</h1>", unsafe_allow_html=True)




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
        'Brasiliense-DF': "https://upload.wikimedia.org/wikipedia/pt/thumb/3/3a/Brasiliense_Futebol_Clube.png/120px-Brasiliense_Futebol_Clube.png",
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
        'Portuguesa': "https://logodetimes.com/times/portugal/selecao-portuguesa-de-futebol-4096.png",
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


# Criar caixa de seleção de Ano

st.markdown("<h3 style='text-align: center;'>Saiba mais sobre os confrontos entre:</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    # Criar caixa de seleção dde Clubes mandantes
    df_club_man = sorted(df_data["time_man"].value_counts().index)
    club_man = st.selectbox("Selecione um clube:", df_club_man)
with col3:
   # Criar caixa de seleção de Clubes
    df_club_vis = df_data[df_data["time_man"]==club_man]
    df_club_vis = sorted(df_club_vis["time_vis"].value_counts().index)
    club_vis = st.selectbox("Selecione seu adversário:", df_club_vis)


logo = get_club_logo(club_man)


# def create_cont_results(df_data,club_man,club_vis):

club_man_filtered = df_data[(df_data["time_man"] == club_man) & (df_data["time_vis"] == club_vis)]
club_vis_filtered = df_data[(df_data["time_man"] == club_vis) & (df_data["time_vis"] == club_man)]

# Vitórias do mandante em casa
vic_man = len(club_man_filtered[club_man_filtered["gols_man"] > club_man_filtered["gols_vis"]])

# Vitórias do mandante fora
vic_vis = len(club_vis_filtered[club_vis_filtered["gols_vis"] > club_vis_filtered["gols_man"]])
vict_man_man = vic_man + vic_vis
# Vitórias do visitante em casa
vic_man_vis = len(club_man_filtered[club_man_filtered["gols_man"] < club_man_filtered["gols_vis"]])

# Vitórias do visitante em casa
vic_vis_vis = len(club_vis_filtered[club_vis_filtered["gols_vis"] < club_vis_filtered["gols_man"]])
vict_vis_vis = vic_man_vis + vic_vis_vis

draws_man = len(club_man_filtered[club_man_filtered["gols_man"] == club_man_filtered["gols_vis"]])
draws_vis = len(club_vis_filtered[club_vis_filtered["gols_vis"] == club_vis_filtered["gols_man"]])

draws = draws_man  + draws_vis

tot_games = draws+ vict_man_man + vict_vis_vis

col1, col2, col3 = st.columns(3)
with col1:
    st.warning(f"**Total de Jogos:** {tot_games}")



col1, col2, col3 = st.columns(3)
with col1:
    st.success(f"**Vitórias:** {vict_man_man}")
with col2:
   st.info(f"**Empates:** {draws}")
with col3:
    st.success(f'**Vitórias:** {vict_vis_vis}')

col1, col2, col3 = st.columns(3)
with col1:
    st.success(f"**Vitórias em casa:** {vic_man}")

with col3:
   st.success(f'**Vitórias em casa:** {vic_vis_vis}')

col1, col2, col3 = st.columns(3)
with col1:
    st.success(f"**Vitórias fora:** {vic_vis}")

with col3:
    st.success(f'**Vitórias fora:** {vic_man_vis}')

df_confr = pd.merge(club_man_filtered, club_vis_filtered, how = 'outer')
df_clone=df_confr[:] 

# "time_man",'gols_man',"gols_vis",'time_vis',

df_confr=df_clone[['data','rodada',"tecnico_man", "time_man", "time_vis",'gols_man','gols_vis',"tecnico_vis","estadio"]]
# df_confr


df_pos = df_confr.sort_values(by='data').copy()
columns = ['data','rodada',"tecnico_man", "time_man", "time_vis",'gols_man','gols_vis',"tecnico_vis","estadio"]

df_pos['data'] = pd.to_datetime(df_pos['data'])

df_tabela = df_pos[columns]

df_tabela.loc[:, "Placar"] = (df_pos["time_man"] + " " + df_pos["gols_man"].astype(float).fillna(0).astype('int64').astype(str) + " x " +  df_pos["gols_vis"].astype(float).fillna(0).astype('int64').astype(str) + " " + df_pos["time_vis"])
df_tabela.loc[:,"data"] = df_tabela["data"].dt.strftime('%d/%m/%y')
df_tabela.loc[:,"Logo_man"] = df_tabela["time_man"].apply(get_club_logo)
df_tabela.loc[:,"Logo_vis"] = df_tabela["time_vis"].apply(get_club_logo)


# Select and rename columns for the final table
df_tab = df_tabela[["data", "rodada",
                    "Logo_man", "Placar", "Logo_vis",'estadio']]

df_tab.rename(columns={"data": "Data do Jogo", "rodada": "Rodada", "Logo_man": "Escudo Mandante", "Logo_vis": "Escudo Visitante","estadio":"Estádio"}, inplace=True)
    
st.dataframe(df_tab,
             column_config={
                 "Escudo Mandante": st.column_config.ImageColumn(),
                 "Escudo Visitante": st.column_config.ImageColumn(),
             }, height=500, width=800,
             hide_index=True)


st.divider()


