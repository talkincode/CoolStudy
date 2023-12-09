import random
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class MindmapItem(BaseModel):
    title: str = Field(..., title="Mindmap Title as root node,required", description="Mindmap Title, Root node",
                       example="Python 学习")
    structure: Dict[str, List[str]] = Field(...,
                                            title="Mindmap Structure data, required",
                                            description="Mindmap Structure data, "
                                                        "The title value must be included in the structure's keys",
                                            example={
                                                "Python 学习": ["基础知识", "高级主题"],
                                                "基础知识": ["变量", "数据类型", "控制流"],
                                                "高级主题": ["面向对象", "装饰器", "迭代器"]
                                            })


def generate_light_color(pcolor: str):
    """生成比给定颜色更浅的颜色"""
    r, g, b = int(pcolor[1:3], 16), int(pcolor[3:5], 16), int(pcolor[5:7], 16)

    # 增加每个颜色分量，使之更接近255
    # 比如，可以使用原始值与255之间的75%点而不是50%
    r = int(r + 0.65 * (255 - r))
    g = int(g + 0.65 * (255 - g))
    b = int(b + 0.65 * (255 - b))

    return '#%02x%02x%02x' % (r, g, b)


def generate_random_dark_color():
    """
    生成随机深色的函数。
    通过确保RGB值不会太高，从而生成深色调。
    """
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    return f'#{r:02x}{g:02x}{b:02x}'


# 改进的思维导图构建函数
def build_mind_map(graph, node, parent, structure, level=0, parent_color=None):
    # 根据层级设置样式
    if level == 0:  # 根节点
        node_color = generate_random_dark_color()
        graph.node(node, style='filled', color=node_color, fontsize="21", fontname='Noto Sans',
                   fontcolor='white',
                   shape='ellipse', peripheries="2", label=node)
    elif level == 1:  # 第二层节点
        node_color = generate_random_dark_color()
        graph.node(node, style='filled', color=node_color, fontsize="18", fontname='Noto Sans',
                   fontcolor='white',
                   shape='egg', peripheries="2", label=node)
    elif level == 2:  # 第三层节点
        node_color = generate_light_color(parent_color)
        graph.node(node, style='filled', color=node_color, fontsize="16", shape='Mrecord', fontname='Noto Sans',
                   label=node)
    else:  # 其他层级
        node_color = generate_light_color(parent_color)
        graph.node(node, style='filled', color=node_color, fontsize="14", shape='Mrecord', fontname='Noto Sans',
                   label=node)

    # 连接节点
    if parent:
        graph.edge(parent, node, penwidth='3.0', arrowhead="diamond", color=node_color)

    # 递归构建子节点
    for child in structure.get(node, []):
        build_mind_map(graph, child, node, structure, level=level + 1,
                       parent_color=node_color if level == 1 else parent_color)
