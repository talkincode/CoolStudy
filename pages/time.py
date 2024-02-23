# Streamlit Timeline Component Example
from libs.llms import create_timeline_data_by_openai
import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# Define the options for the timelist selectbox
timelist_options = [...]

# Add the timeline to the timelist selectbox
timelist_options.append("Timeline")

# Create the timelist selectbox
timelist = st.sidebar.selectbox('timeline', timelist_options)

# load data
user_input = st.chat_input("输入用处")
if user_input:
    with st.spinner("生成中..."):
        airesp = create_timeline_data_by_openai(user_input)
        if timelist == "Timeline":
            timeline(airesp, height=800)

    