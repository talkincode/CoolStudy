import json

import streamlit as st
import sys
import os
from dotenv import load_dotenv
from libs.knowledge import search_knowledge
from libs.prompts import get_system_message
from libs.msal import msal_auth
from libs.llms import openai_streaming
from libs.session import PageSessionState

sys.path.append(os.path.abspath('..'))
load_dotenv()


def get_chatbot_page(botname, knowledge_name, is_edu=False, show_libs=False):
    page_state = PageSessionState(botname)
    # st.sidebar.markdown("# 💡Python 编程导师")

    # 用于存储对话记录, 第一条为欢迎消息
    page_state.initn_attr("messages", [])
    # 用于标记上一条用户消息是否已经处理
    page_state.initn_attr("last_user_msg_processed", True)
    # 用于标记流式输出是否结束
    page_state.initn_attr("streaming_end", True)
    page_state.initn_attr("quick_command", "")

    def end_chat_streaming():
        """当停止按钮被点击时执行，用于修改处理标志"""
        page_state.streaming_end = True
        page_state.last_user_msg_processed = True

    def start_chat_streaming():
        """当开始按钮被点击时执行，用于修改处理标志"""
        page_state.streaming_end = False
        page_state.last_user_msg_processed = False

    def on_input_prompt(iprompt: str):
        if iprompt.strip() == "":
            return
        page_state.chat_prompt = iprompt
        start_chat_streaming()
        page_state.add_chat_msg("messages", {"role": "user", "content": page_state.chat_prompt})
        with st.chat_message("user"):
            st.write(page_state.chat_prompt)

    for msg in page_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])



    # 用户输入
    if not page_state.last_user_msg_processed:
        st.chat_input("请等待上一条消息处理完毕", disabled=True)
    else:
        if prompt := st.chat_input("输入你的问题"):
            on_input_prompt(prompt)

    if is_edu:
        qprompt = st.sidebar.selectbox("快速命令列表", ["", "/plan", "/start", "/continue",
                                                        "/test choice", "/test program", "/result",
                                                        "/help", "/config 中文",
                                                        ], index=0)
        if st.sidebar.button("发送命令"):
            on_input_prompt(qprompt)

    stop_action = st.sidebar.empty()
    if not page_state.streaming_end:
        stop_action.button('停止输出', on_click=end_chat_streaming, help="点击此按钮停止流式输出")

    # 用户输入响应，如果上一条消息不是助手的消息，且上一条用户消息还没有处理完毕
    if (page_state.messages
            and page_state.messages[-1]["role"] != "assistant"
            and not page_state.last_user_msg_processed):
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # 检索知识库
                kmsg = search_knowledge(knowledge_name, page_state.chat_prompt)
                if kmsg != "" and show_libs:
                    st.expander("📚 知识库检索结果", expanded=False).markdown(kmsg)
                sysmsg = get_system_message(botname, kmsg)
                response = openai_streaming(sysmsg, page_state.messages[-10:])
                # 流式输出
                placeholder = st.empty()
                full_response = ''
                page_state.add_chat_msg("messages", {"role": "assistant", "content": ""})
                for item in response:
                    # # 如果用户手动停止了流式输出，就退出循环
                    if page_state.streaming_end:
                        break
                    text = item.content
                    if text is not None:
                        full_response += text
                        placeholder.markdown(full_response)
                        page_state.update_last_msg("messages", {"role": "assistant", "content": full_response})
                placeholder.markdown(full_response)

        stop_action.empty()
        end_chat_streaming()

    st.sidebar.download_button('导出对话历史',
                               data=json.dumps(page_state.messages, ensure_ascii=False),
                               file_name="chat_history.json", mime="application/json")

    if st.sidebar.button('清除对话历史'):
        page_state.messages = []
