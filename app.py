import pandas as pd
import streamlit as st
import plotly.express as px


#read the csv file here
df =pd.read_csv('vehicles_us.csv')


#use the st.checkbox


st.markdown("<h1 style='text-align: center;'>Vehicles</h1>", unsafe_allow_html=True)

start_button = st.button('Run')

if st.checkbox("Show only cars prices less than $20k"):
    df = df[df['price'] < 20000]

df.head()

df.tail()


#st.write(px.histogram(...))
fig = px.histogram(df,x='price')
st.plotly_chart(fig)
#st.write(px.scattr(....))
fig = px.scatter(df,x='odometer',y='price',color='condition')
##fig.show()
st.plotly_chart(fig)

# Load example DataFrame
#df = px.data.carshare()

st.title("Carshare Data Visualization")

# Checkbox to switch plots
show_scatter = st.checkbox("Show scatter plot (odometer vs price)", value=False)

if show_scatter:
    fig = px.scatter(
        df,
        x="odometer",
        y="price",
        color="condition",
        title="Odometer vs Price by Condition",
        labels={"odometer": "Odometer (miles)", "price": "Price ($)"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    fig = px.histogram(
        df,
        x="price",
        title="Price Distribution",
        nbins=30,
        labels={"price": "Price ($)"}
    )
    st.plotly_chart(fig, use_container_width=True)

