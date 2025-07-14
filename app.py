import pandas as pd
import streamlit as st
import plotly.express as px







st.markdown("<h1 style='text-align: center;'>Vehicles</h1>", unsafe_allow_html=True)

start_button = st.button('Run')

# Example vehicle data (replace with your actual DataFrame loading code)
df = pd.DataFrame([
    {"make": "Ford", "model": "Bronco", "year": 2025, "price": 40000},
    {"make": "Jeep", "model": "Wrangler", "year": 2025, "price": 38000},
    {"make": "Toyota", "model": "Camry", "year": 2024, "price": 25000},
    # … more rows …
])

if st.button("Run"):
    # Filter for Ford or Jeep
    filtered = df[df["make"].isin(["Ford", "Jeep"])]
    
    # Optional: further filters in the sidebar
    makes = st.sidebar.multiselect("Make", options=filtered["make"].unique(), default=filtered["make"].unique())
    years = st.sidebar.multiselect("Year", options=filtered["year"].unique(),
                                   default=filtered["year"].unique())
    
    filtered = filtered[
        filtered["make"].isin(makes) &
        filtered["year"].isin(years)
    ]
    
    st.dataframe(filtered)
#use the st.checkbox
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

