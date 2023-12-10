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






