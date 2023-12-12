import streamlit as st


st.set_page_config(page_title="Streamlit 组件学习", page_icon="🤖")


st.sidebar.markdown("# 🤖Streamlit 组件学习")

with st.expander("全部代码"):
    st.code(open(__file__, "r", encoding="utf-8").read(), language="python")

with st.expander("文本组件"):
    st.text('固定宽度的文本')
    st.markdown('markdown 格式文本 _Markdown_')
    st.latex(r'''公式 e^{i\pi} + 1 = 0 ''')
    st.write('Python 对象')
    st.write(['st', 'is <', 3])
    st.title('标题文本')
    st.header('副标题文本')
    st.subheader('二级副标题文本')
    st.code('st.code("Hello, Streamlit!") # 代码块')
    st.write(['st', 'is <', 3])
    
    st.latex(r'''公式 \pi''')
   


import streamlit as st
import time
chinken = st.number_input("输入黑字", min_value=0, value=0, step=1)

for i in range(chinken):
    # 创建一个占位符
    placeholder = st.empty()    
    # 初始时在占位符位置显示一些文本
    placeholder.code('st.code("Hello, Streamlit!") # 代码块')
        # 创建一个占位符
    placeholder = st.empty()
    # 等待几秒钟
    time.sleep(2)

    # 然后更新占位符位置的内容
    placeholder.text("你干嘛嘿嘿有")
    time.sleep(2)
        # 创建一个占位符
    placeholder = st.empty()
    # 初始时在占位符位置显示一些文本
    placeholder.text("鸡你太美")
        # 创建一个占位符
    placeholder = st.empty()
