import streamlit as st


def show_page():
    # 创建页面标题
    st.title("计算器")
    # 创建页面副标题
    st.subheader("这是一个简单的计算器")
    # 创建页面描述
    st.markdown("""
    这是第一版本的计算器，他的用处非常不大，勉强可以计算加法，但是还是可以计算很大的数字的加法。用起来不是很方便。
    但是，这是一个可以正常运行的计算器，这是一个很好的开始。BoyJiang同学在老师的指导下已经可以独立完成这个版本的计算器了。
    对于 streamlit 的玩法已经有了初步了解， 在这个过程中对很多基本的语法，数据类型有了一次难得的实战。
    """)

    # 创建代码块显示当前代码
    with st.expander("查看代码"):
        st.code(open(__file__, "r", encoding="utf-8").read(), language="python")

    # 创建一个分割线
    st.divider()

    # 定义当前页面持久变量 left_val 表示加号左边的数字
    if "left_val" not in st.session_state:
        st.session_state["left_val"] = ""

    # 定义当前页面持久变量 right_val 表示加号右边的数字
    if "right_val" not in st.session_state:
        st.session_state["right_val"] = ""

    # 定义当前页面持久变量 pos 表示当前输入的位置是左边还是右边
    if "pos" not in st.session_state:
        st.session_state["pos"] = "left"

    # 创建三个并排的列， 用于显示输入框
    colin1, colin2, colin3 = st.columns(3)
    # 创建左边输入框
    left_box = colin1.text_input("left", st.session_state["left_val"])
    # 创建右边输入框
    right_box = colin2.text_input("right", st.session_state["right_val"])
    # 创建结果输入框，暂时使用一个空的容器
    resultbox = colin3.container()

    def update_val(value):
        # 定义一个函数，用于更新输入框的值
        pos = st.session_state["pos"]
        if pos == "left" and st.session_state["left_val"] not in ["0"]:
            st.session_state["left_val"] += value
        elif pos == "right" and st.session_state["right_val"] not in ["0"]:
            st.session_state["right_val"] += value
        st.rerun()

    # 创建一个九宫格的矩阵， 来模拟计算器的界面
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    col10, col0, col12 = st.columns(3)

    # 创建一个函数，用于创建数字按钮
    def create_number_button(column, number):
        if column.button(str(number)):
            update_val(str(number))

    # 创建数字按钮序列，用语创建数字按钮
    cols = [col0, col1, col2, col3, col4, col5, col6, col7, col8, col9]

    # 遍历数字按钮序列，创建数字按钮
    for col in cols:
        create_number_button(col, cols.index(col))

    # 创建加号按钮
    if col10.button("加"):
        st.session_state["pos"] = "right"

    # 创建等号按钮， 点击等号按钮时，计算结果
    if col12.button("="):
        try:
            lval = int(st.session_state["left_val"])
        except:
            lval = 0

        try:
            rval = int(st.session_state["right_val"])
        except:
            rval = 0

        result = str(lval + rval)
        resultbox.text_input("结果", result)

    # 创建清除按钮，点击清除按钮时，清除输入框的值
    if st.button("清除"):
        st.session_state["left_val"] = ""
        st.session_state["right_val"] = ""
        st.session_state["pos"] = "left"
        st.rerun()
