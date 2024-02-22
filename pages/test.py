import streamlit as st
import contextlib
import io
password = st.text_input("请输入密码:", type="password")
code = st.text_area("请输入代码", height=200)
st.code(code, language="python")
if st.button("运行"):
    output = io.StringIO()
    error = io.StringIO()

    # 重定向标准输出和错误输出
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):#std表示标准输出，std表示标准错误输出
        try:
            exec(code)
        except Exception as e:
            st.error(f"执行代码时出错: {e}")
    # 显示标准输出和错误输出
    st.text("输出:")
    st.code(output.getvalue(), language="python")
    st.text("错误:")
    st.code(error.getvalue(), language="python")