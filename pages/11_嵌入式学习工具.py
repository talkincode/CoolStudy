import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page
sys.path.append(os.path.abspath('..'))
load_dotenv()
os.getenv('YOUR_ENV_VARIABLE')
st.markdown("## 🌐 酷学 嵌入式学习工具")
st.markdown("一个精通嵌入式的人工智能导师，可以解决任何嵌入式问题")
get_chatbot_page("coolstudy_bot365", "coolstudy_bot365", mr_ranedeer=True)