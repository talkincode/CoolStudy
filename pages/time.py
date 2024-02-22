# Streamlit Timeline Component Example
from libs.llms import create_timeline_data_by_openai
import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
user_input = st.sidebar.text_input("输入用处")
if st.sidebar.button("生成时间线"):
    with st.spinner("生成中..."):
        airesp = create_timeline_data_by_openai(user_input)
        timeline(airesp, height=800)

