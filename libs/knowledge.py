import requests
import os


# 定义知识库名称和对应的集合名称
knowledge_dictionary = {
    "未选择": "",
}


def search_knowledge(collection, query):
    """Define a knowledge base retrieval function"""
    gpt_address = os.getenv("GPT_SERVICE_ADDRESS")
    api_token = os.getenv("GPT_SERVICE_TOKEN")
    url = f"{gpt_address}/knowledge/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    payload = {
        "collection": collection,
        "query": query
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error searching knowledge: {response.text}"
    data = response.json()

    def fmt(v):
        return f'**Score**: {v["score"]}\n\n{v["content"]}\n\n---\n\n'

    return "\n\n".join([fmt(v) for v in data["result"]["data"]])

