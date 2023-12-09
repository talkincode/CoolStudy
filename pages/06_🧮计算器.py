import streamlit as st


st.title("计算器")

st.markdown("""
这是一个中学生学习编程的实践，通过 streamlit 实现一个简单的计算器。这个项目以初级版本开始，逐步迭代，最终实现一个功能完善的计算器。
""")

tab1, tab2, tab3 = st.tabs(["第一版", "第二版", "第三版"])

with tab1:
    from apps import calculator_01
    calculator_01.show_page()

with tab2:
    st.write("第二版")

with tab3:
    st.write("第三版")
