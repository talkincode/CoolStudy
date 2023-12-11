import os.path
from jinja2 import FileSystemLoader, Environment
from jinja2 import Template

_current_file_path = os.path.abspath(__file__)
assets_path = os.path.join(os.path.dirname(_current_file_path), "assets")

file_loader = FileSystemLoader(assets_path)
env = Environment(loader=file_loader)


def get_content_from(name: str) -> str:
    """
    Reads the content from a Markdown file.

    :param name: The name of the Markdown file.
    :return: The content of the Markdown file as a string.
    """
    filepath = os.path.join(assets_path, name + ".md")
    return open(filepath, "r", encoding="utf-8").read()


commoon_knowledge_prompt = get_content_from("knowledge_prompt")

mr_ranedeer = get_content_from("Mr_Ranedeer")


def get_mr_ranedeer_message(depth: str) -> str:
    """
    以给定的深度呈现 Randeer 先生的信息。

    :param depth: 用户学历深度级别。
    :type depth: str
    :return: 呈现了 Randeer 先生的信息。
    :rtype: str
    """
    tpl = Template(mr_ranedeer)
    return tpl.render({
        "depth": depth,
    })


def get_system_message(name, kmsg: str, depth) -> str:
    """
    :param name：要渲染的模板文件的名称。
    :param kmsg：要包含在系统消息中的知识消息。
    :param depth：消息的深度，默认为“Middle School”。
    :return：以字符串形式呈现的系统消息。
    """
    data = {"mr_ranedeer_message": get_mr_ranedeer_message(depth)}
    if kmsg not in "":
        data["knowledge_messages"] = f"""\n{commoon_knowledge_prompt}\n'''\n{kmsg}\n'''\n"""
    systpl = env.get_template(f"{name}.md")
    sysmsg = systpl.render(data)
    print(sysmsg)
    return sysmsg


if __name__ == "__main__":
    print(get_system_message("codeboy", "test"))

