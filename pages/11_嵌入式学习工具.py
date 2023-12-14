import streamlit
import sys
import os
from dotenv import load_dotenv
from libs.llms import openai_streaming
sys.path.append(os.path.abspath('..'))
load_dotenv()


st.markdown("## 🌐 酷学 嵌入式学习工具")
st.markdown("一个精通嵌入式的人工智能导师，可以解决任何嵌入式问题")

get_chatbot_page("coolstudy_bot365", "coolstudy_bot365", mr_ranedeer=True)
