import streamlit as st
from datetime import datetime

st.write("Hello, world!")
#just write a number on a screen
#3 + 7
#"Hello, baby"
#"Hello, baby" if True else "Hello, man"

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
formatted_datetime

# on original load, the button has a state of False
# when you click the button, on next run,
# the state changes to True
pressed1 = st.button("Button 1") # pressed1 is a boolean of button state during this run
print("First:", pressed1)

pressed2 = st.button("Button 2")
print("Second:", pressed2)