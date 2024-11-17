import os
import streamlit as st
from datetime import datetime
import pandas as pd

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime

# Dataframe section
st.subheader("Dataframe")
df = pd.DataFrame({
	'Name': ['John', 'Smith', 'Paul', 'Alice'],
	'Age': [23, 45, 32, 28],
    "Occupation": ["Engineer", "Doctor", "Teacher", "Nurse"]
})
st.dataframe(df)

# Data Editor section (editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df) 

st.divider()
