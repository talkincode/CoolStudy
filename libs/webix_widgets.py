import streamlit as st
import json
import streamlit.components.v1 as components
from string import Template

def create_webix_list(data, height=300):
    # 转换数据为 JSON 格式
    json_data = json.dumps(data)

    # 定义 HTML 模板
    html_template = Template('''
    <html>
    <head>
        <script type="text/javascript" src="//cdn.webix.com/edge/webix.js"></script>
        <link rel="stylesheet" type="text/css" href="//cdn.webix.com/edge/webix.css">
    </head>
    <body>
        <script>
            var listData = $data;
            webix.ready(function() {
                webix.ui({
                    view: "list",
                    data: listData
                });
            });
        </script>
    </body>
    </html>
    ''')

    # 填充模板
    html_code = html_template.substitute(data=json_data)

    # 使用 Streamlit 的 HTML 组件来展示这个 Webix List
    components.html(html_code, height=height)
