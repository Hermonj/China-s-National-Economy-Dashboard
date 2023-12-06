import streamlit as st
import pandas as pd
import numpy as np

st.title("China's National Economy Dashboard")
st.header("GDP growth, GDP per capita, inflation rate, unemployment rate, and current account balance.")
st.markdown("The dashboard provides visualizations of key economic indicators for China's national economy. It aims to help users understand the historical trends and current status of the Chinese economy.")

# Read the CSV file
data = pd.read_csv("ChinaNationalEconomyData.csv")

# Create a simple dashboard with basic plots
st.title("China's National Economy Dashboard")
st.subheader("Key Economic Indicators")

# Real GDP Growth
st.line_chart(data["Real GDP growth (Annual percent change)"])

# GDP per Capita
st.line_chart(data["GDP per capita, current prices (U.S. dollars per capita)"])

# Inflation Rate
st.line_chart(data["Inflation rate, average consumer prices (Annual percent change)"])

# Unemployment Rate
st.line_chart(data["Unemployment rate (Percent)"])

# Current Account Balance
st.line_chart(data["Current account balance U.S. dollars (Billions of U.S. dollars)"])

st.subheader("Growth Rates and Financial Metrics")

# 5-year GDP Growth Rate
st.text(data["5-year GDP growth rate"].mean())

# 5-year Inflation Rate
st.text(data["5-year Inflation rate"].mean())

# 5-year Unemployment Rate
st.text(data["5-year Unemployment rate"].mean())

# 5-year Current Account Balance
st.text(data["5-year Current account balance"].mean())
