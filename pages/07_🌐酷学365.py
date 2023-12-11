import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page

sys.path.append(os.path.abspath('..'))
load_dotenv()


st.markdown("## 🌐 酷学 365")
st.markdown("博学多才的人工智能学习导师，可以帮助学生解决各种学习上的问题")

get_chatbot_page("coolstudy_bot365", "coolstudy_bot365", mr_ranedeer=True)
