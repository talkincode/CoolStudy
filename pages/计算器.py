import streamlit as st

st.title("计算器")

st.subheader("这是一个简单的计算器")

st.divider()


if "left_val" not in st.session_state:
    st.session_state["left_val"] = ""

if "right_val" not in st.session_state:
    st.session_state["right_val"] = ""

if "pos" not in st.session_state:
    st.session_state["pos"] = "left"

colin1, colin2,colin3 = st.columns(3)
left_box = colin1.text_input("left", st.session_state["left_val"])
right_box = colin2.text_input("right", st.session_state["right_val"])
resultbox = colin3.container()

def update_val(value):
    pos = st.session_state["pos"]
    if pos == "left" and st.session_state["left_val"] not in ["0"]:
        st.session_state["left_val"] += value
    elif pos == "right" and st.session_state["right_val"] not in ["0"]:
        st.session_state["right_val"] += value

    st.rerun()
    

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)
col10,col0,col12 = st.columns(3)


if col1.button("1"):
    update_val("1")
    
if col2.button("2"):
    update_val("2")

if col3.button("3"):
    update_val("3")

if col4.button("4"):
    update_val("4")

if col5.button("5"):
    update_val("5")


if col6.button("6"):
    update_val("6")


if col7.button("7"):
    update_val("7")


if col8.button("8"):
    update_val("8")


if col9.button("9"):
    update_val("9")


if col0.button("0"):
    update_val("0")

if col10.button("加"):
   st.session_state["pos"] = "right"


if col12.button("="):
    try:
        lval = int(st.session_state["left_val"])
    except:
        lval = 0

    try:
        rval = int(st.session_state["right_val"])
    except:
        rval = 0

    result= str(lval+rval)
    resultbox.text_input("结果",result)


if st.button("清除"):
    st.session_state["left_val"] = ""
    st.session_state["right_val"] = ""
    st.session_state["pos"]= "left"
    st.rerun()

