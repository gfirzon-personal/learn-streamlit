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
    name1 = st.text_input("Enter your first name")
    birth_date = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)

    if birth_date:
        age = datetime.now().year - birth_date.year
        if birth_date.month > datetime.now().month or (birth_date.month == datetime.now().month and birth_date.day > datetime.now().day):
            age -= 1
        st.write(f"Your calculated age is {age} years.")

    #print(name, age)
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if not name1 or not birth_date:
            st.warning("Please fill out all fields.")
        else:
            st.success(f"Thnak you for submitting the form, {name1}! You age is {age}.")
            st.balloons()
            