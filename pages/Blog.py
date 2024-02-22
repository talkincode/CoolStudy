import streamlit as st
import os

st.title('博客')

class MyBlog:

    def __init__(self):
        self.filedir = 'blogs'
        if not os.path.exists(self.filedir):
            os.mkdir(self.filedir)   
            

    def add(self,title,content):
        with open(f'{self.filedir}/{title}.txt','w') as firs:
            firs.write(content)


    def get(self,filename):
        with open(f'{self.filedir}/{filename}','r') as firs:
            return firs.read()
    
    
    def list(self):
        return os.listdir(self.filedir)


    def delete(self,title):
        os.remove(f'{self.filedir}/{title}')
    
    
        
    def update(self,title,content):
        with open(f'{self.filedir}/{title}.txt','w') as firs:
            firs.write(content)
            
blog = MyBlog()

tab1, tab2 = st.tabs([ "readblog", "writeblog"])
with tab1:
    blog_list = blog.list()
    
    for item in blog_list:
        st.markdown(item)
        if st.button('删除',key=f'key_{item}'):
            blog.delete(item)
            st.rerun()
        st.markdown(blog.get(item))
        st.divider()    
    
   

with tab2:
    title = st.text_input('标题')
    content = st.text_area('内容')  
    if st.button('提交'):
        blog.add(title,content)
        st.success('提交成功')
        st.rerun()

