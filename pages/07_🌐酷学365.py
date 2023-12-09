import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page
from libs.prompts import get_cs365_sysmsg

sys.path.append(os.path.abspath('..'))
load_dotenv()


st.sidebar.markdown("# 🌐 酷学 365")
st.sidebar.markdown("一个学习辅助型人工智能助手，可以帮助学生解决各种学习上的问题")

get_chatbot_page("coolstudy_bot365", "coolstudy_bot365", get_cs365_sysmsg)
