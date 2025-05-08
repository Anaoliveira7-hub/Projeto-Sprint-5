import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer") # criar um histograma
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo