import streamlit as st
import pandas as pd
import numpy as np

st.title("China's National Economy Dashboard")
st.header("GDP growth, GDP per capita, inflation rate, unemployment rate, and current account balance.")
st.markdown("The dashboard provides visualizations of key economic indicators for China's national economy. It aims to help users understand the historical trends and current status of the Chinese economy.")

# Read the CSV file
data = pd.read_csv("ChinaNationalEconomyData.csv")
