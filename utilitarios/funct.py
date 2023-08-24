# Buscar escudo do clube
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

################## Definir cor para gráfico   ############################

def get_club_color(club):
    color_mapping = {
        'América-MG'or 'Chapecoense' or 'Coritiba FC'or 'Cuiabá-MT'or 'Fluminense' or 'Goiás'or 'Goiás EC'or 'Guarani'or 'Juventude'or 'Palmeiras': "green",
        'América-RN' or 'Athletico-PR' or 'Atlético-GO'or 'Atlético-PR'or 'EC Vitória' or 'Flamengo'or 'Internacional'or 'Joinville-SC'or 'Náutico'or 'Paraná'or 'Portuguesa'or 'RB Bragantino' or 'Santa Cruz' or 'Sport Recife'  or 'São Paulo':"red",
        'Atlético-MG' or 'Botafogo'or 'Ceará SC' or 'Figueirense FC' or 'Corinthians'or 'Ponte Preta'or 'Santos'or 'Santos FC'or 'Vasco da Gama':"black",
        'Avaí FC' or 'Barueri' or 'CSA'or 'Cruzeiro'or 'EC Bahia'or 'CSA' or 'Fortaleza'or 'Grêmio'or 'Ipatinga FC'or 'Paysandu SC'or 'São Caetano':"blue",
        'Brasiliense-DF'or 'Criciúma EC':"yellow"

}
    return color_mapping.get(club, "black")
