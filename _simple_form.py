from datetime import datetime
import os
import streamlit as st
from utils.time import get_formatted_datetime
from core.sidebar import create_sidebar

## Form Elements
min_date = datetime(1900, 1, 1)
max_date = datetime.now()

st.title("User Information Form")

# Call the function to create the sidebar
create_sidebar()

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
    #"location": None,
}

with st.form(key='user_form'):
    # Add a text input for the user to enter their name
    form_values["name"] = st.text_input("Enter your name")
    # Add a number input for the user to enter their height
    form_values["height"] = st.number_input("Enter your height (cm)")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["dob"] = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)

    #print(name, age)
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill out all fields.")
        else:
            st.balloons()
            st.write("Form submitted successfully!")
            for key, value in form_values.items():
                st.write(f"{key}: {value}")