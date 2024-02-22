import streamlit
import random

key = input("请输入一个单词")
Englishword = {'word': key}
# Automatically save the word in Englishword dictionary
Englishword['word'] = key
print(Englishword)

