import streamlit as st
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime

st.title('Super Simple Streamlit App')
st.header('This is a header')
st.subheader('This is a subheader')
st.markdown('This is **some** markdown')
st.markdown('This is _some_ markdown')
st.markdown('This is **_some_** markdown')
st.caption('This is a caption')

code_example = """
def hello():
    print("Hello, world!")
"""
st.code(code_example, language='python')

st.divider()