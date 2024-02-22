import streamlit as st
import os

st.title('C++教材')

import streamlit as st
import os

class Mylesson:

    def __init__(self):
        self.filedir = 'lessons'
        if not os.path.exists(self.filedir):
            os.mkdir(self.filedir)

    def add(self, title, content):
        with open(f'{self.filedir}/{title}.txt', 'w') as file:
            file.write(content)

    def get(self, title):
        filename = f'{self.filedir}/{title}.txt'
        if not os.path.exists(filename):
            # 如果文件不存在，创建一个内容为c++教材的文件
            with open(filename, 'w') as file:
                file.write('c++教材')
            return "文件不存在，已创建一个新的空文件。"
        else:
            with open(filename, 'r') as file:
                return file.read()

    def list(self):
        return os.listdir(self.filedir)

    def delete(self, title):
        os.remove(f'{self.filedir}/{title}.txt')

lesson = Mylesson()

lesson_list = lesson.list()

tab1, tab2 = st.tabs(["阅读课程", "课程列表"])

with tab1:
    if lesson_list:
        selected_lesson = st.selectbox("选择课程", lesson_list)
        if st.button('显示课程内容'):
            content = lesson.get(selected_lesson.replace('.txt', ''))
            if "文件不存在" in content:
                st.warning(content)
            else:
                st.text(content)
    else:
        st.write("当前没有可用的课程。")

with tab2:
    st.write("课程列表")
    if lesson_list:
        for item in lesson_list:
            st.markdown(item)
            if st.button(f'删除{item}', key=f'delete_{item}'):
                lesson.delete(item.replace('.txt', ''))
                st.experimental_rerun()
    else:
        st.write("当前没有可用的课程进行显示或删除。")
