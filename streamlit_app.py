import streamlit as st
import pandas as pd
import numpy as np

st.title("China's National Economy Dashboard")
st.header("GDP growth, GDP per capita, inflation rate, unemployment rate, and current account balance.")
st.markdown("The dashboard provides visualizations of key economic indicators for China's national economy. It aims to help users understand the historical trends and current status of the Chinese economy.")


dataframe = pd.DataFrame(np.random.randn(10, 20),
  columns = ('col %d' % i
    for i in range(20)))
st.write(dataframe)

st.write('This is a line_chart.')
st.line_chart(dataframe)

st.write('This is a area_chart.')
st.area_chart(dataframe)

st.write('This is a bar_chart.')
st.bar_chart(dataframe)

st.write('Map data')
data_of_map = pd.DataFrame(
  np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
  columns = ['latitude', 'longitude'])
st.map(data_of_map)


image = Image.open('picture.jpg')
st.image(image, caption = 'This is a picture', use_column_width = True)