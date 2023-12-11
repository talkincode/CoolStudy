import streamlit as st
from urllib.parse import quote as urlencode

st.set_page_config(page_title="CoolStudy 应用面板", page_icon="🎛️")

st.sidebar.markdown("# 🎛️ 应用面板")

# List of apps
apps = [
    {
        "name": "💥 方程式杀手",
        "remark": "`一个简单的工具，用于化简和解决方程式`",
        "link": urlencode("方程式杀手"),
    },
    {
        "name": "🔬 图像分析",
        "remark": "`通过 AI 分析图像中的内容，提供有用的信息`",
        "link": urlencode("图像分析"),
    },
    {
        "name": "✨ 智能思维导图",
        "remark": "`通过 AI 模型分析，生成智能思维导图`",
        "link": urlencode("智能思维导图"),
    },
    {
        "name": "🎙️ 语音转录",
        "remark": "`通过 AI 模型识别语音内容，转录文本，并支持合成新语音`",
        "link": urlencode("语音转录"),
    },
    {
        "name": "🌐 酷学365",
        "remark": "`一个 AI 学习助手， 解答学习上的任何问题`",
        "link": urlencode("酷学365"),
    },
    {
        "name": "🐍 Python_编程导师",
        "remark": "`一个 Python 学习助手，可以设计学习计划、解答问题`",
        "link": urlencode("Python_编程导师"),
    },
    {
        "name": "🎨 图像生成",
        "remark": "`通过 AI 模型生成图像，包括人脸、动漫人物、风景等`",
        "link": urlencode("图像生成"),
    },
    {
        "name": "🤖 Streamlit_组件学习",
        "remark": "`一个 Streamlit 组件学习应用案例`",
        "link": urlencode("Streamlit_组件学习"),
    },
]

cols = st.columns(3)
# Iterating over the apps to create buttons in the UI
for i, app in enumerate(apps):
    # Determine which column to place the app based on index
    col = cols[i % 3]
    # Create a button for each app in the respective column
    with col.expander(app['name'], expanded=True):
        st.markdown(app['remark'])
        link = app['link']
        name = app['name']
        link_html = f"""
    <a href="{link}" target="_self" style="
        text-decoration: none;
        color: RoyalBlue;
        background-color: Gainsboro;
        padding: 7px 14px;
        border-radius: 5px;
        font-size: 14px;
        font-weight: bold;
        ">
    {name}
    </a>
"""
        st.markdown(link_html, unsafe_allow_html=True)

        # st.link_button(app['name'], app['link'])
