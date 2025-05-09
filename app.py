import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button('Criar um gráfico de dispersão') #criar um botão

st.header('Relação entre Preço e Quilometragem Percorrida')
st.markdown(
    "<p style='font-size: 14px;'>"
    "Este gráfico de dispersão mostra como o preço dos veículos varia de acordo com a quilometragem percorrida (hodômetro). "
    "Em geral, espera-se que veículos com maior quilometragem tenham preços mais baixos, mas também é possível identificar exceções "
    "ou padrões por ano, tipo de combustível e outros fatores."
    "</p>",
    unsafe_allow_html=True)

if hist_button: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer") # criar um histograma
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")  # criar gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True) 


#criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer') 
    fig = px.histogram(car_data, x="odometer") # criar um histograma
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly inte

if build_scatter: # se a caixa de seleção for selecionada
    st.write('Criando um gráfico de dispersão para a coluna odometer')
    fig = px.scatter(car_data, x="odometer", y="price")  # criar gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True) 
