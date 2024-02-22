import streamlit as st
import os

st.title('C++教材')

class Mylesson:

    def __init__(self):
        self.filedir = 'lessons'
        if not os.path.exists(self.filedir):
            os.mkdir(self.filedir)

    def add(self, title, content):
        with open(f'{self.filedir}/{title}.md', 'w') as firs:
            firs.write(content)

    def get(self, title):
        filename = f'{self.filedir}/{title}.md'
        if os.path.exists(filename):
            with open(filename, 'r') as firs:
                return firs.read()
        else:
            return "文件不存在"

    def list(self):
        files = os.listdir(self.filedir)
        md_files = [file for file in files if file.endswith('.md')]
        return md_files

    def delete(self, title):
        os.remove(f'{self.filedir}/{title}.md')

lesson = Mylesson()
lesson_list = lesson.list()

tab1, tab2 = st.tabs(["阅读课程", "课程列表"])

with tab1:
    selected_lesson = st.selectbox("选择课程", lesson_list)
    if st.button('显示课程内容'):
        content = lesson.get(selected_lesson.replace('.md', ''))
        if content == "文件不存在":
            st.error(content)
        else:
            st.text(content)

with tab2:
    st.write("课程列表")
    for item in lesson_list:
        st.markdown(item)
        if st.button(f'删除{item}', key=f'delete_{item}'):
            lesson.delete(item.replace('.md', ''))
            st.experimental_rerun()
            