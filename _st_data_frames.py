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

# Static table section
st.subheader("Static Table")
st.table(df)

# Metrics section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=df["Age"].mean(), delta=1)

# JSON and Dict section
st.subheader("JSON and Dict")
sample_dict = {
    "name": "John",
    "age": 23,
    "sills": ["Python", "JavaScript", "SQL", "Data Science", "Machine Learning"]
}
st.json(sample_dict)

#st.divider()
