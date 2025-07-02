import pandas as pd
import streamlit as st
import plotly.express as px


#read the csv file here
df =pd.read_csv('vehicles_us.csv')


#use the st.checkbox

st.header('Vehicles')

number_of_trials = st.slider('Milage', 1, 1000, 10)
start_button = st.button('Run')

df.head()

df.tail()


#st.write(px.histogram(...))
fig = px.histogram(df,x='price')
st.plotly_chart(fig)
#st.write(px.scattr(....))
fig = px.scatter(df,x='odometer',y='price',color='condition')
##fig.show()
st.plotly_chart(fig)

df['condition'].value_counts().plot(kind='bar')

df.groupby('model')['price'].mean().sort_values(ascending=False)[:20].plot(kind='bar')


df['model'].value_counts()[:20].plot(kind='bar')

df['price'].value_counts()[:20].plot(kind='bar')