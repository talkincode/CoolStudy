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

