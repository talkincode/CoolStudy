import os.path


def get_sysmsg_from(name: str) -> str:
    current_file_path = os.path.abspath(__file__)
    filepath = os.path.join(os.path.dirname(current_file_path), "assets", name + ".md")
    return open(filepath, "r", encoding="utf-8").read()


commoon_knowledge_prompt = """
// Knowledge Base Usage Guidelines

The following is a list of potentially relevant information retrieved from the knowledge base that you should 
prioritize and determine if it is relevant enough to the user's input.
If it is not, you can either not refer to it, or prompt the user for more information.
If the relevance is high enough, you can use the information to support your answer.
"""


def get_system_message(name, kmsg: str) -> str:
    sysmsg = get_sysmsg_from(name)
    kmsgs = f"""\n\n{commoon_knowledge_prompt}\n\n'''\n{kmsg}\n'''\n"""
    if kmsg not in "":
        return sysmsg + kmsgs
    return sysmsg


