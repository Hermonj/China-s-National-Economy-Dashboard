import streamlit as st
import pandas as pd
import numpy as np

st.title("China's National Economy Dashboard")
st.header(
    "GDP growth, GDP per capita, inflation rate, unemployment rate, and current account balance 202242260041-ROMHA TEKLE."
)

st.markdown(
    "The dashboard provides visualizations of key economic indicators for China's national economy. It aims to help users understand the historical trends and current status of the Chinese economy."
)

# Read the CSV file
data = pd.read_csv("Economy_Dashboard2.csv")

# Real GDP Growth
st.write('This is GDP growth.')
st.line_chart(data["GDP growth"])

# Inflation Rate
st.write('This is GDP per capita.')
st.area_chart(data["GDP per capita"])

# Inflation Ratest.bar_chart(data["Inflation rate"])
st.write('This is GDP, current prices.')
st.area_chart(data["GDP, current prices"])

# Inflation Rate
st.write('This is GDP based on PPP.')
st.bar_chart(data["GDP based on PPP"])

# Inflation Rate
st.write('This is Implied PPP conversion rate.')
st.line_chart(data["Implied PPP conversion rate"])


#sidebar
with st.sidebar:
    with st.echo():
        st.write("We are building China-s-National-Economy-Dashboard ")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


#columns 01
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Trade War")
   st.image("https://images.pexels.com/photos/4386371/pexels-photo-4386371.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

with col2:
   st.header("National Economy")
   st.image("https://images.pexels.com/photos/210607/pexels-photo-210607.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

with col3:
   st.header("Stock Exchange")
   st.image("https://images.pexels.com/photos/745243/pexels-photo-745243.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

#column 02
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a national chart")
col1.line_chart(data)

col2.subheader("A narrow column with the national data")
col2.write(data)
