import os
import streamlit as st
from utils.time import get_formatted_datetime

def create_sidebar():
    st.sidebar.title("Sidebar")
    image_path = os.path.join(os.getcwd(), 'static', 'me.png')
    st.sidebar.image(image_path, use_container_width=False, width=200)

    st.sidebar.write("This is the sidebar.")
    st.sidebar.write(get_formatted_datetime())