import os
import streamlit as st
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime

st.divider()

image_path = os.path.join(os.getcwd(), 'static', 'bg.png')
st.image(image_path, use_column_width=True)