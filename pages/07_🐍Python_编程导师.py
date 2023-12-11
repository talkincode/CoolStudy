import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page
from libs.prompts import get_codeboy_sysmsg
from libs.session import PageSessionState

sys.path.append(os.path.abspath('..'))
load_dotenv()


st.sidebar.markdown("# 💡Python 编程导师")

get_chatbot_page("codeboy", "codeboy", get_codeboy_sysmsg, is_edu=True)
