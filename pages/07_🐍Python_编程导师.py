import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page

sys.path.append(os.path.abspath('..'))
load_dotenv()


st.markdown("## 💡Python 编程导师")

get_chatbot_page("codeboy", "codeboy", mr_ranedeer=True)
