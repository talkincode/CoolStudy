import json
import uuid

import streamlit as st
import sys
import os

from graphviz import Digraph

from libs import get_data_dir
from libs.llms import create_mindmap_data_by_openai
from libs.mindmap import MindmapItem, build_mind_map
from libs.session import PageSessionState

# 假设你的 Streamlit 应用位于 'CoolStudy' 目录下
sys.path.append(os.path.abspath('..'))

data_dir = get_data_dir()

page_state = PageSessionState("ai_mindmap")

page_state.initn_attr("mindmap_json", None)
page_state.initn_attr("mindmap_file", None)

st.sidebar.markdown("# ✨智能思维导图️️")


def gen_mindmap(engine_name):
    if page_state.mindmap_json is None:
        return
    # 使用 model_validate 方法创建 MindmapItem 实例
    item = MindmapItem.model_validate(page_state.mindmap_json)
    graph = Digraph(comment=item.title, engine=engine_name)
    graph.attr(overlap='scale', splines='compound')
    build_mind_map(graph, item.title, None, structure=item.structure)
    output_path = os.path.join(data_dir, uuid.uuid4().hex)
    graph.render(output_path, format='png', cleanup=True)
    page_state.mindmap_file = output_path


prompt = st.text_area("输入思维导图内容提示语：", "Python 基础语法", key="ai_mindmap_prompt", height=60)

if st.button("生成思维导图"):
    with st.spinner("生成中..."):
        airesp = create_mindmap_data_by_openai(prompt)
        page_state.mindmap_json = json.loads(airesp)
        gen_mindmap(page_state.engine or "fdp")

if page_state.mindmap_json is not None:
    with st.expander("思维导图数据"):
        st.json(page_state.mindmap_json)


def on_engine_change():
    if page_state.mindmap_json is not None:
        with st.spinner("开始生成思维导图..."):
            gen_mindmap(page_state.engine)


engine = st.sidebar.selectbox("选择渲染引擎", ["dot", "neato", "fdp", "sfdp", "twopi", "circo", "patchwork", "osage"],
                              key="ai_mindmap_engine",
                              on_change=on_engine_change
                              )

if page_state.mindmap_file is not None:
    st.image(page_state.mindmap_file + ".png")
