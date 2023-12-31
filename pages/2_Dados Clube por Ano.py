import streamlit as st
import matplotlib.pyplot as plt
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

st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")

col1, col2 = st.columns(2)
with col1:
   # Criar caixa de seleção de Clubes
    clubs = sorted(df_data["time_man"].value_counts().index)
    club = st.selectbox("Clube", clubs)

with col2:
    # Criar caixa de seleção de Ano
    years = df_data[df_data["time_man"] == club]
    years = sorted(years["ano_campeonato"].unique(), reverse=True)
    year = st.selectbox("Ano", years)


# col1, col2 = st.columns(2)
# with col1:
#     # Criar caixa de seleção de Ano
#     years = sorted(df_data["ano_campeonato"].value_counts().index, reverse=True)
#     year = st.selectbox("Ano", years)
# with col2:
#    # Criar caixa de seleção de Clubes
#     clubs = df_data[df_data["ano_campeonato"] == year]
#     clubs = sorted(clubs["time_man"].value_counts().index)
#     club = st.selectbox("Clube", clubs)


################## Buscar escudo do clube ##################


def get_club_logo(club):
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
    return logo_mapping.get(club, "")
################## alterar nomes para pesquisas nos dados do Kaggle ##################


def get_club_masc(club):
    logo_mapping = {
        'América-MG': "http://acervodocoelho.com.br/wp-content/uploads/2015/02/COELHAOOOOO.jpg",
        "America-MG":"http://acervodocoelho.com.br/wp-content/uploads/2015/02/COELHAOOOOO.jpg",
        'América-RN': "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8tqVZPG9gO0UfawuANF2_jYCTBPNFNQl-Id77_TUm&s",
        'Athletico-PR': "https://static.wixstatic.com/media/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png/v1/fill/w_566,h_797,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png",
        'Atlético-PR': "https://static.wixstatic.com/media/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png/v1/fill/w_566,h_797,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png",
        'Atletico-PR':"https://static.wixstatic.com/media/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png/v1/fill/w_566,h_797,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/5cfd0b_05f186beba0f4018b2fea735d67454a9~mv2.png", 
        'Atlético-GO': "http://2.bp.blogspot.com/-VGEzrdXjxes/T3Wor-1tG0I/AAAAAAAACv8/DJW2hKd7YXY/s1600/mascote+new.JPG",
        "Atletico-GO":"http://2.bp.blogspot.com/-VGEzrdXjxes/T3Wor-1tG0I/AAAAAAAACv8/DJW2hKd7YXY/s1600/mascote+new.JPG",
        "Atletico-MG":"https://image-service.onefootball.com/transform?w=840&h=630&dpr=2&image=https%3A%2F%2Fmercadodofutebol.com%2Fwp-content%2Fuploads%2F2023%2F07%2F52819054337_b1c95bd988_c-2.jpg",
        'Atlético-MG': "https://image-service.onefootball.com/transform?w=840&h=630&dpr=2&image=https%3A%2F%2Fmercadodofutebol.com%2Fwp-content%2Fuploads%2F2023%2F07%2F52819054337_b1c95bd988_c-2.jpg",
        'Avaí FC': "https://static.wixstatic.com/media/5cfd0b_0cd86a5268ff4283babf581b2745967a~mv2.png/v1/fill/w_566,h_797,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/5cfd0b_0cd86a5268ff4283babf581b2745967a~mv2.png",
        "Avai":"https://static.wixstatic.com/media/5cfd0b_0cd86a5268ff4283babf581b2745967a~mv2.png/v1/fill/w_566,h_797,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/5cfd0b_0cd86a5268ff4283babf581b2745967a~mv2.png",
        'Barueri': "https://www.campeoesdofutebol.com.br/distintivos/gremio_barueri_mascote_2015.jpg",
        'Botafogo': "https://s2-ge.glbimg.com/jT0ZNSNGlED1jqSj0HqwHYu9utw=/0x0:1024x808/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2022/v/j/ZCbkWvSJeiRBh6AfON0g/biriba.jpg",
        "Botafogo-RJ": "https://s2-ge.glbimg.com/jT0ZNSNGlED1jqSj0HqwHYu9utw=/0x0:1024x808/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2022/v/j/ZCbkWvSJeiRBh6AfON0g/biriba.jpg",
        'Brasiliense-DF': "https://www.brasiliensefc.com.br/wp-content/uploads/2019/08/mascote_bse.png",
        'CSA': "https://omunicipio.com.br/wp-content/uploads/2021/05/confianca-se-serie-b-2021-especial-csa-mini.png",
        'Ceará SC': "https://www.cearasc.com/media/img/noticias/vovo_O4hxCD9.jpg",
        "Ceara": "https://www.cearasc.com/media/img/noticias/vovo_O4hxCD9.jpg",
        'Chapecoense': "https://chapecoense.com/wp-content/uploads/2022/07/indio-mascote.jpg",
        'Corinthians': "https://amascoteria.com.br/wp-content/uploads/2017/05/Mascote_3d_Corinthians_A-768x768.jpg",
        "Coritiba": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibmTOlwzbJn1TO1gH4yt342vy1LHF0wLPrIpGw_KGspqVk5da-HmAcXSDUB61l_wOOS4RV4ZuWgewEAzSp-i876lfgBKHTWlgJf8GCGSrDr0rX5SJ9r6jXjdrVKIfM2_Hs6gfeP7ypC8cCOG7N0Ie0WLp8wKeU7jXUPuTog4geQgQWXJzOHludQwAgGA/s16000/mascote_do_coritiba.jpg",       
        'Coritiba FC': "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibmTOlwzbJn1TO1gH4yt342vy1LHF0wLPrIpGw_KGspqVk5da-HmAcXSDUB61l_wOOS4RV4ZuWgewEAzSp-i876lfgBKHTWlgJf8GCGSrDr0rX5SJ9r6jXjdrVKIfM2_Hs6gfeP7ypC8cCOG7N0Ie0WLp8wKeU7jXUPuTog4geQgQWXJzOHludQwAgGA/s426/mascote_do_coritiba.jpg",
        # 'Criciúma EC': "-5.png",
        # 'Criciuma': "-5.png",
        # 'Cruzeiro': "-256.png",
        # 'Cuiabá-MT': ".png",
        # "Cuiaba": ".png", 
        # "EC Bahia": "ng",
        # "Bahia": "ng",
        # "Vitoria": "56.png",       
        # 'EC Vitória': "56.png",
        # 'Figueirense FC': "irense-256.png",
        # "Figueirense":"irense-256.png",    
        # 'Flamengo': "-256.png",
        # 'Fluminense': "ense-256.png",
        # 'Fortaleza': "za-256.png",
        # 'Goiás': "te-clube-4096.png",
        # 'Goiás EC': "te-clube-4096.png",
        # 'Goias': "te-clube-4096.png",  
        # 'Grêmio': ".png",
        # 'Gremio': ".png",
        # 'Guarani': "56.png",
        # 'Internacional': "ernacional-256.png",
        # 'Ipatinga FC': "
        # 'Joinville-SC': "x-Joinville_Esporte_Clube_logo.svg.png",
        # 'Juventude': "de-256.png",
        # 'Náutico': "56.png",
        # "Nautico": "56.png",
        # 'Palmeiras': "as-256.png",
        # 'Paraná': ".png",
        # "Parana": ".png",
        # "Paysandu":"-5.png",
        # 'Paysandu SC': "-5.png",
        # "Paysandu": "-5.png",
        # 'Ponte Preta': "-preta-256.png",
        # 'Portuguesa': "guesa-de-futebol-4096.png",
        # 'RB Bragantino': "go-red-bull-bragantino-256.png",
        # "Bragantino": "go-red-bull-bragantino-256.png",
        # 'Santa Cruz': "cruz-256.png",
        # 'Santo André': "-andre-256.png",
        # "Santo Andre":"-andre-256.png",
        # 'Santos': ".png  ",
        # 'Santos FC': ".png  ",
        # 'Sport Recife': "b_Recife.svg.png",
        # "Sport":"b_Recife.svg.png",
        # 'São Caetano': "aetano-256.png",
        # "Sao Caetano":"aetano-256.png",
        # 'São Paulo': "lo-256.png",
        # 'Sao Paulo':"lo-256.png",
        # 'Vasco da Gama': "co-da-gama-256.png",
        # 'Vasco': "co-da-gama-256.png",
    }
    return logo_mapping.get(club, "")


def get_club_name(club):
    club_mapping = {
        'América-MG': "America-MG",
        'Atlético-PR': "Athletico-PR",
        'Atlético-GO': "Atletico-GO",
        'Atlético-MG': "Atletico-MG",
        'América-RN': "America-RN",
        'Avaí FC': "Avai",
        'Botafogo': "Botafogo-RJ",
        'Ceará SC': "Ceara",
        'Coritiba FC': "Coritiba",
        'Cuiabá-MT': "Cuiaba",
        "EC Bahia": "Bahia",
        'EC Vitória': "Vitoria",
        'Figueirense FC': "Figueirense",
        'Goiás' : 'Goias',
        'Goiás EC': 'Goias',
        'Grêmio': 'Gremio',
        'Náutico': "Nautico",
        'Paraná': "Parana",
        'Paysandu SC': "Paysandu",
        'RB Bragantino': "Bragantino",
        'Santo André': "Santo Andre",
        'Santos' : 'Santos',
        'Santos FC': 'Santos',
        'Sport Recife': "Sport",
        'São Caetano': "Sao Caetano",
        'São Paulo': 'Sao Paulo',

        'Barueri':'Barueri' ,
        'Botafogo':  'Botafogo',
        "Botafogo-RJ": 'Botafogo',
        'Brasiliense-DF':'Brasiliense-DF',
        'CSA':  'CSA',
        'Chapecoense': 'Chapecoense',
        'Corinthians': 'Corinthians',
        "Cuiaba": "Cuiaba",
        "EC Bahia":  "Bahia",
        "Bahia":  "Bahia",
        "Vitoria":"Vitoria",
        "Figueirense":"Figueirense",
        'Flamengo': 'Flamengo',
        'Fluminense':'Fluminense',
        'Fortaleza': 'Fortaleza',
        'Guarani': 'Guarani',
        'Internacional': 'Internacional',
        'Ipatinga FC': 'Ipatinga FC',
        'Joinville-SC':'Joinville-SC',
        'Juventude': 'Juventude',
        "Nautico":  "Nautico",
        'Palmeiras': 'Palmeiras',
        "Parana": "Parana",
        "Paysandu": "Paysandu",
        'Ponte Preta': 'Ponte Preta',
        'Portuguesa': 'Portuguesa',
        "Bragantino":  "Bragantino",
        'Santa Cruz':'Santa Cruz',
        "Santo Andre":"Santo Andre",
        'Santos':  'Santos',
        'Santos FC': 'Santos FC',
        'Sport Recife': 'Sport Recife',
        "Sport":"Sport",
        "Sao Caetano":"Sao Caetano",
        'Sao Paulo':'Sao Paulo',
        'Vasco da Gama': 'Vasco da Gama',
        'Vasco da Gama': 'Vasco',
    }
    return club_mapping .get(club, club)
################## Definir cor para gráfico ############################


def get_club_color(club):
    color_mapping = {
        'América-MG': "green",
        'Chapecoense': "green",
        'Coritiba FC': "green",
        'Cuiabá-MT': "green",
        'Fluminense': "green",
        'Goiás': "green",
        'Goiás EC': "green",
        'Guarani': "green",
        'Juventude': "green",
        'Palmeiras': "green",
        'América-RN': "red",
        'Athletico-PR': "red",
        'Atlético-GO': "red",
        'Atlético-PR': "red",
        'EC Vitória': "red",
        'Flamengo': "red",
        'Internacional': "red",
        'Joinville-SC': "red",
        'Náutico': "red",
        'Paraná': "red",
        'Portuguesa': "red",
        'RB Bragantino': "red",
        'Santa Cruz': "red",
        'Sport Recife': "red",
        'São Paulo': "red",
        'Atlético-MG': "black",
        'Botafogo': "black",
        'Ceará SC': "black",
        'Figueirense FC': "black",
        'Corinthians': "black",
        'Ponte Preta': "black",
        'Santos': "black",
        'Santos FC': "black",
        'Vasco da Gama': "black",
        'Avaí FC': "blue",
        'Barueri': "blue",
        'CSA': "blue",
        'Cruzeiro': "blue",
        'EC Bahia': "blue",
        'Fortaleza': "blue",
        'Grêmio': "blue",
        'Ipatinga FC': "blue",
        'Paysandu SC': "blue",
        'São Caetano': "blue",
        'Brasiliense-DF': "yellow",
        'Criciúma EC': "yellow"
    }
    return color_mapping.get(club,"black")

################## Apresentar tabela com os confrontos realizados por campeonato ############################


#################  Selecionar campeonatos por ano #################

### filtro especial para campeonatos de 2020 e 2021 que foram situações especiais devido a COVID  ###
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

#########   Estádio e média de público  ##################

def estadios_clube_ano(df_data, year, club):
    # Filtra o DataFrame com base no ano do campeonato e no clube
    filtered_df = df_data[(df_data['ano_campeonato'] == year) & (df_data['time_man'] == club)]
    
    # Remove espaços em branco no início e no final da coluna 'estadio'
    filtered_df['estadio'] = filtered_df['estadio'].str.strip()
    
    # Obtém uma lista dos estádios únicos em que o clube jogou
    estadios = filtered_df['estadio'].unique()
    
    return estadios

# Chama a função para obter a lista de estádios
estadios = estadios_clube_ano(df_data, year, club)
estadios_str = ', '.join(estadios)

# Imprime a lista de estádios

############# Criar tabela com os jogos com condicional para abaixo de 2006 ###################

def create_match_table(df_data, year, club):
    if year <= 2006:
        max_id, min_id = localId(df_brasFul,year)
        club = get_club_name(club)
        filtered_df = df_brasFul[(df_brasFul['ID'] >= min_id) & (df_brasFul['ID'] <= max_id)]
        df_pos = filtered_df[(filtered_df["mandante"] == club) | (filtered_df["visitante"] == club)]
        df_pos = df_pos.sort_values(by='rodata')
        columns = ["data", "rodata", "mandante", "visitante"]
        df_pos['data'] = pd.to_datetime(df_pos['data'])
        
        df_tabela = df_pos[columns]

        df_tabela["mandante_Placar"] = df_pos["mandante_Placar"].astype('int64')
        df_tabela["visitante_Placar"] = df_pos["visitante_Placar"].astype('int64')
        
        df_tabela.loc[:,"Placar"] = df_pos["mandante"] + " " + df_pos["mandante_Placar"].astype(str) + " x " + df_pos["visitante_Placar"].astype(str) + " " + df_pos["visitante"]
        df_tabela.loc[:,"data"] = df_tabela["data"].dt.strftime('%d/%m')
        df_tabela.loc[:,"Logo_man"] = df_tabela["mandante"].apply(get_club_logo)  # Usando a coluna 'mandante' ao invés de 'time_man'
        df_tabela.loc[:,"Logo_vis"] = df_tabela["visitante"].apply(get_club_logo) # Usando a coluna 'visitante' ao invés de 'time_vis'
        
        # Selecionando e renomeando colunas para a tabela final
        df_tab = df_tabela[["data", "rodata", "Logo_man", "Placar", "Logo_vis"]].copy()
        df_tab.rename(columns={"data": "Data do Jogo", "rodata": "Rodada", "Logo_man": "Escudo Mandante", "Logo_vis": "Escudo Visitante"}, inplace=True)
   
    else:
        df_pos = df_data[(df_data["ano_campeonato"] == year) & (
            (df_data["time_man"] == club) | (df_data["time_vis"] == club))]

        df_pos = df_pos.sort_values(by='rodada').copy()
        columns = ["data", "rodada", "publico", "time_man", "time_vis"]
        
        df_pos['data'] = pd.to_datetime(df_pos['data'])

        df_tabela = df_pos[columns]

        df_tabela.loc[:, "Placar"] = (df_pos["time_man"] + " " + df_pos["gols_man"].astype(float).fillna(0).astype('int64').astype(str) + " x " +  df_pos["gols_vis"].astype(float).fillna(0).astype('int64').astype(str) + " " + df_pos["time_vis"])
        df_tabela.loc[:,"data"] = df_tabela["data"].dt.strftime('%d/%m')
        df_tabela.loc[:,"Logo_man"] = df_tabela["time_man"].apply(get_club_logo)
        df_tabela.loc[:,"Logo_vis"] = df_tabela["time_vis"].apply(get_club_logo)
        df_tabela.loc[:,"publico"] = df_tabela["publico"].astype(int).astype(str)

        # Select and rename columns for the final table
        df_tab = df_tabela[["data", "rodada", "Logo_man", "Placar", "Logo_vis", "publico"]]
        
        df_tab.rename(columns={"data": "Data do Jogo", "rodada": "Rodada", "Logo_man": "Escudo Mandante", "Logo_vis": "Escudo Visitante", "publico": "Público"}, inplace=True)
    
    return df_tab  # Retorna o DataFrame df_tabela

# Chama a função create_match_table e atribui o resultado a df_tab
df_tab = create_match_table(df_data, year, club)
logo = get_club_logo(club)
colorLine = get_club_color(club)
clubGols = get_club_name(club)
table = create_match_table(df_data, year, club)
masc = get_club_masc(club)

# Calcular número de rodadas do campeonato
df_year = df_data[df_data["ano_campeonato"] == year]
ultRod = df_year["rodada"].max()

# Ver posição do clube ao fim do campeonato
club_location_man = df_year[(df_year["rodada"] == ultRod) & (
    df_year["time_man"] == club)]["colocacao_man"]

# Filtrar para o clube como time visitante na última rodada
club_location_vis = df_year[(df_year["rodada"] == ultRod) & (
    df_year["time_vis"] == club)]["colocacao_vis"]

# Verificar se o clube estava como time mandante ou visitante e obter a colocação correspondente
if not club_location_man.empty:
    value = club_location_man.values[0]
    club_location = str(int(value)) if not pd.isna(value) else "N/A"
elif not club_location_vis.empty:
    value = club_location_vis.values[0]
    club_location = str(int(value)) if not pd.isna(value) else "N/A"
else:
    club_location = "N/A"


######## Calcular vitórias, derrotas e empates ########
def create_cont_results(df_data, year, club):
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

    return victories, empates, derrotas


victories, empates, derrotas = create_cont_results(df_data, year, club)


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


total_gols, total_gols_sofridos, saldo = create_data_gols(df_data, club, year)

##### Criar tabela final do campeonato ###########

def create_create_table(df_data, year):
    # Cria um DataFrame vazio com as colunas desejadas
    df_table_games = pd.DataFrame(columns=[
                                  "Clube", "Pontos", "Vitórias", "Empates", "Derrotas", "Gols Marcados", "Gols Sofridos", "Saldo"])

    # Seleciona os clubes que jogaram como mandante no ano especificado, filtra e ordena em ordem alfabética
    clubs = sorted(df_data[df_data["ano_campeonato"]== year]["time_man"].unique())

    for club in clubs:

        victories, empates, derrotas = create_cont_results(df_data, year, club)
        total_gols, total_gols_sofridos, saldo = create_data_gols(df_data, club, year)
        pontos = (victories * 3) + empates  # Calcula os pontos corretamente
        new_Header = {"Clube": club, "Pontos": pontos, "Vitórias": victories, "Empates": empates, "Derrotas": derrotas, "Gols Marcados": total_gols,
                    "Gols Sofridos": total_gols_sofridos, "Saldo": saldo}
        df_table_games = pd.concat([df_table_games, pd.DataFrame([new_Header])], ignore_index=True)
    # Ordena o DataFrame por pontos de forma decrescente
    df_table_games = df_table_games.sort_values(by=["Pontos", "Vitórias", "Saldo"], ascending=[False, False, False])
    # Adiciona a coluna de sequência numérica
    df_table_games.insert(0, "Sequência", range(1, len(df_table_games) + 1))

    return df_table_games


# Chama a função para criar a tabela
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
            styles.append('background-color:  rgba(93, 178, 48, 0.3);')
        elif i >= len(s) - 4:
            styles.append('background-color: rgba(243, 9, 9, 0.3)')
        else:
            styles.append('')
    return styles

styled_resulting_table_games = resulting_table_games.style.apply(highlight_rows)






#################  Contagem de gols por ano #################

filtered_df = df_brasGols[(df_brasGols['partida_id'] >= (
    min_id)) & (df_brasGols['partida_id'] <= (max_id))]
filtered_df = filtered_df[(df_brasGols['clube']) == clubGols]

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
    jogadores_contagem_ordenada.items(), columns=['Atleta', 'Gols'])



#################  Contagem de cartões por ano #################
filtered_df = df_brasCards[(df_brasCards['partida_id'] >= (
    min_id)) & (df_brasCards['partida_id'] <= (max_id))]
filtered_df = filtered_df[filtered_df['clube'] == clubGols].reset_index(drop=True)


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


####################### Criar gráfico   #######################
def plot_evolucao_posicao(df_data, club, year, colorLine):
    if year <= 2006:
        return '❗❗❗❗❗❗  Dados indisponíveis  ❗❗❗❗❗❗❗❗'
    
    df_posRod = df_data[(df_data["time_man"] == club) &
                        (df_data["ano_campeonato"] == year)]
    df_posVis = df_data[(df_data["time_vis"] == club) &
                        (df_data["ano_campeonato"] == year)]

    
    df_new = pd.concat([
        df_posRod[['rodada', 'colocacao_man']].rename(
            columns={'colocacao_man': 'posicao'}),
        df_posVis[['rodada', 'colocacao_vis']].rename(
            columns={'colocacao_vis': 'posicao'})
        
    ])
    df_new["posicao"] = df_new["posicao"].astype(float).fillna(0).astype('int64')
    
    df_new = df_new.sort_values('rodada').reset_index(drop=True)

        
    if df_new.empty:
        return 'Dados indisponíveis para o gráfico'

    # Plotar gráfico de linha
    plt.figure(figsize=(8, 3))  # Definir o tamanho da figura
    plt.plot(df_new['rodada'], df_new['posicao'],
             marker='', color=(f'{colorLine}'), lw=0.5)
    plt.xlabel('Rodada')
    plt.ylabel('Posicao')
    plt.title(f'Evolução do {club} no Brasileiro {year}')
    plt.axhline(y=1, color='green', linestyle='-', lw=0.8)
    plt.axhline(y=20, color='black', linestyle='-', lw=0.5)
    plt.axhline(y=17, color='red', linestyle='--',
                 lw=0.5, label="Zona de Rebaixamento")
    plt.legend(loc='lower right')

    # Ajustar eixo Y do maior para o menor
    plt.ylim(22, 0)

    # Inserir rótulo de dados
    for index, row in df_new.iterrows():
        plt.text(row['rodada'], row['posicao'], str(
            row['posicao']), ha='center', va='bottom', fontsize=8)
    # Remover bordas do gráfico
    plt.axis('off')
    # plt.plot( '--', label='Linha Tracejada')

# Adicionar uma legenda ao gráfico
    plt.legend()
    plt.grid(True)  
    
    return plt

plot = plot_evolucao_posicao(df_data, club, year, colorLine)



####################### FRONT  ##############

################## formatação do cabeçalho da página Logo + nome do clube ##################
col1, col2, col3 = st.columns(3)
with col1:
    st.image(logo, width=90)
with col2:
    st.title(f"{club}")

# with col3:
#     st.image(masc, width=130)

col1, col2, col3 = st.columns(3)
try:
    with col1:
        st.write(f"**Posição Final:** {club_location}")
except:
    with col1:
        st.write("**Posição Final: - **")

with col2:
    st.markdown(f"**Brasileirão** {year}")


######### Colunas de vitórias, Empates e derrotas  ##################
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Vitórias:** {victories}")
with col2:
    st.markdown(f"**Empates:** {empates}")
with col3:
    st.markdown(f'**Derrotas:** {derrotas}')

########## Colunas de Gols marcados, Gols sofridos e Saldo  ##################
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Gols marcados:** {total_gols}")
with col2:
    st.markdown(f"**Gols sofridos:** {total_gols_sofridos}")
with col3:
    st.markdown(f'**Saldo:** {saldo}')

st.write(f"**Estádios:** {estadios_str}")

st.divider()
######### Tabela de Artilheiros do clube #######
try:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Artilheiros do Campeonato**")
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

######### Plotagem do gráfico #######
if isinstance(plot, str):
    st.write(plot)  # Mostrar mensagem de dados indisponíveis
else:
    st.pyplot(plot)

st.divider()


######### Plotagem da tabela de jogos #######
st.markdown(f"**Tabela de Jogos do campeonato** ")
st.dataframe(table,
             column_config={
                 "Escudo Mandante": st.column_config.ImageColumn(),
                 "Escudo Visitante": st.column_config.ImageColumn(),
             }, height=500, width=800,
             hide_index=True)


st.divider()

######### Plotagem da tabela final do campeonato #######
st.markdown(f"**Tabela do campeonato** ")
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
