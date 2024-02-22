import streamlit as st
import sys
import os
from dotenv import load_dotenv
from apps.chatbot import get_chatbot_page

sys.path.append(os.path.abspath('..'))
load_dotenv()

st.markdown("## 💡Python 编程导师")

# 创建一个列表来存储对话
chat_history = []

# 获取聊天机器人的回答
bot_response = get_chatbot_page("codeboy", "codeboy", mr_ranedeer=True)

# 将聊天机器人的回答添加到对话历史中
chat_history.append(f"机器人: {bot_response}")

# 在网页上显示对话历史
for message in chat_history:
    st.text(message)