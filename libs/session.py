import streamlit as st


# 定义一个用于管理Streamlit会话状态的类
class PageSessionState:
    def __init__(self, prefix):
        # 初始化函数，每个会话状态实例都有一个唯一的前缀
        self._prefix = prefix

    def initn_attr(self, key: str, default_value: object):
        # 初始化属性，如果属性不存在，则设置为默认值
        if not hasattr(st.session_state, self.getkey(key)):
            st.session_state[self.getkey(key)] = default_value

    def add_chat_msg(self, key: str, value: object):
        # 添加聊天消息，如果键不存在，则创建一个新列表
        if not hasattr(st.session_state, self.getkey(key)):
            st.session_state[self.getkey(key)] = []
        try:
            st.session_state[self.getkey(key)].append(value)
        except:
            # 如果尝试添加到非列表类型，则抛出异常
            raise AttributeError("Cannot append to non-list attribute")

    def update_last_msg(self, key: str, value: object):
        # 更新最后一条消息，如果键不存在，则创建一个新列表并添加消息
        if not hasattr(st.session_state, self.getkey(key)):
            st.session_state[self.getkey(key)] = []
            st.session_state[self.getkey(key)].append(value)
            return
        try:
            st.session_state[self.getkey(key)][-1] = value
        except:
            # 如果尝试更新非列表类型的最后一个元素，则抛出异常
            raise AttributeError("Cannot update last message")

    def __getattr__(self, key):
        # 获取属性的魔术方法，首先检查是不是私有属性 _prefix
        if key == "_prefix":
            return self.__dict__[key]
        # 如果存在于 session_state 中，则返回该属性值
        if self.getkey(key) in st.session_state:
            return st.session_state[self.getkey(key)]
        else:
            # 如果属性不存在，则返回 None
            return None

    def __setattr__(self, key, value):
        # 设置属性的魔术方法
        if key == "_prefix":
            self.__dict__[key] = value
        else:
            st.session_state[self.getkey(key)] = value

    def __delattr__(self, key):
        # 删除属性的魔术方法
        if key == "_prefix":
            raise AttributeError("Cannot delete _prefix attribute")
        # 从 session_state 中删除该属性
        st.session_state.pop(self.getkey(key), None)

    def __contains__(self, key):
        # 判断是否包含某个键的方法
        return self.getkey(key) in st.session_state

    def __getitem__(self, key):
        # 用于通过键获取项的方法
        if key == "_prefix":
            return self.__dict__[key]
        return st.session_state[self.getkey(key)]

    def __setitem__(self, key, value):
        # 用于设置项的方法
        if key == "_prefix":
            self.__dict__[key] = value
        else:
            st.session_state[self.getkey(key)] = value

    def __delitem__(self, key):
        # 用于删除项的方法
        if key == "_prefix":
            raise AttributeError("Cannot delete _prefix attribute")
        st.session_state.pop(self.getkey(key), None)

    def __len__(self):
        # 返回 session_state 的长度
        return len(st.session_state)

    def __iter__(self):
        # 返回 session_state 的迭代器
        return iter(st.session_state)

    def __repr__(self):
        # 返回 session_state 的字符串表示
        return repr(st.session_state)

    def __str__(self):
        # 返回 session_state 的字符串形式
        return str(st.session_state)

    def getkey(self, key):
        # 私有方法，用于获取带有前缀的键名
        return f"{self._prefix}_{key}"
