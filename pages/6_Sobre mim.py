import streamlit as st
st.sidebar.markdown("Desenvolvido por [Douglas Mello ](https://www.linkedin.com/in/douglas-mello-13b70012a/)")

st.sidebar.markdown('''

- [Linkedin](https://www.linkedin.com/in/douglas-mello-13b70012a/)
- [Github](https://github.com/Doug-13)
''', unsafe_allow_html=True)    

col1, col2, col3 = st.columns(3)    
with col1:
    st.image('https://media.licdn.com/dms/image/D4D03AQHfCsdexLdO0A/profile-displayphoto-shrink_100_100/0/1682550966648?e=1698883200&v=beta&t=vy3Qm5QmRQIh-Llg2EE6vm4ouRJMr-24VoJ18zi5jg8', width=140)
with col2:
    st.header('Sobre mim')
st.write('''
Olá, feliz por você estar aqui conhecendo este projeto, meu nome é Douglas, sou apaixonado por programação e análise de dados,gostou? Mande dicas para aperfeiçoarmos este trabalho! ''')
st.write('''Este é meu primeiro trabalho em streamlit e python, e muitas coisas fui aprendendo ao longo da criação.''')
st.write('''Me segue lá no [Linkedin](https://www.linkedin.com/in/douglas-mello-13b70012a/), e me fala o que achou do projeto, ainda está um pouco bagunçado, mas vai melhorar...''')
st.write(''' Ahhhhh e divulga aí, me ajuda a fazer com que este projeto chegue mais longe!!''')

