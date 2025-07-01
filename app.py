import pandas as pd
import streamlit as st
import plotly.express as px


#read the csv file here
data=pd.read_csv('vehicles_us.csv')


#use the st.checkbox

st.header('Vehicles')

number_of_trials = st.slider('Car Names', 1, 1000, 10)
start_button = st.button('Run')



#st.write(px.histogram(...))
fig = px.histogram(data,x='price')
st.plotly_chart(fig)
#st.write(px.scattr(....))
fig = px.scatter(data,x='odometer',y='price',color='condition')
##fig.show()
st.plotly_chart(fig)