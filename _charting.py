from datetime import datetime
import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Chart Elements

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime

# Generate sample data
chart_data = pd.DataFrame(
    #Generates a 20x3 array of random numbers from a standard normal distribution.
    np.random.randn(20, 3), 
    #Converts the array into a pandas DataFrame with columns named 'A', 'B', and 'C'.
    columns=['A', 'B', 'C']
)

# Area Chart section
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart section
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart section
st.subheader("Line Chart")
st.line_chart(chart_data)

# Scatter Plot section
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(50),
    'y': np.random.randn(50)
})
st.scatter_chart(scatter_data)

# Map section
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Pyplot section
st.subheader("Pyplot")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.legend()
st.pyplot(fig)

#st.divider()
