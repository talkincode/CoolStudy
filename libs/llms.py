import base64

from openai import OpenAI
import os


def openai_streaming(sysmsg, historys: list):
    """OpenAI Streaming API"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [
        {"role": "system", "content": sysmsg},
    ]
    for history in historys:
        messages.append(history)
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        stream=True
    )
    for chunk in completion:
        yield chunk.choices[0].delta


# 定义函数来调用 OpenAI GPT-4 Vision API
def openai_analyze_image(prompt_str, imagefs):
    client = OpenAI()
    # 将图像转换为 Base64 编码，这里需要一些额外的处理
    # 假设已经将图像转换为 base64_string
    base64_string = base64.b64encode(imagefs.getvalue()).decode('utf-8')

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_str or "分析图片内容"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "data:image/jpeg;base64," + base64_string,
                            "detail": "high"
                        },
                    },
                ],
            }
        ],
        max_tokens=2000,
    )

    return response.choices[0].message.content


def create_mindmap_data_by_openai(content):
    """通过 OPENAI 生成思维导图数据"""
    sysmsg = """
You are a mind mapping expert tasked with analyzing user input, organizing the responses into a mind map structure, and replying in a correctly formatted json structure with UTF-8 encoded emojis.

- Analyze the user's question and decompose it into sub-questions.
- Organize the answers into a mind map structure with no more than 4 levels of nodes.
- Attach an appropriate emoji directly in the node strings for the first three levels of nodes, ensuring the emojis are directly included in the JSON string in UTF-8 format.
- The root node does not need an emoji, note that the value of the root node is also in the structure, please be consistent
- Node names should not use characters that do not conform to the graphviz node name specification.
- The language of the mind map node should match the user's explicit request or the user's input language (e.g., Chinese for Chinese input, English for English input).
- Reply with the mind map structure in standard JSON format, ensuring all strings are correctly quoted and the overall format is valid JSON.
- For clarity and focus, the total number of nodes should not exceed 50, or the maximum number of nodes specified by the user, if requested by the user.

The json format template:

{
    "title": "root node",
    "structure": {
        "root node": ["node1", "node2"],
        "node1": ["node1-1", "node1-2"],
        "node2": ["node2-1", "node2-2"],
    }
}

    """
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": sysmsg},
            {"role": "user", "content": content},
        ]
    )
    return response.choices[0].message.content



def create_timeline_data_by_openai(content):
    """通过 OPENAI 生成history时间线数据"""
    sysmsg = """
You are a knowledgeable expert tasked with analyzing user input, organizing replies into a timeline structure, and replying with a properly formatted json structure with UTF-8 encoded emoticons.

- If the generated media link must be an address that starts with https and can be accessed normally
- Recognize the input language and the language of the result is the same as the input language
- About 200 words per event
- Generate no less than seven timeline events

The json format template:

{
    "title": {
        "text": {
          "headline": "Welcome to<br>Streamlit Timeline",
          "text": "<p>A Streamlit Timeline component by integrating TimelineJS from Knightlab</p>"
        }
    },
    "events": [
      {
        "start_date": {
          "year": "2016",
          "month":"1"
        },
        "text": {
          "headline": "TimelineJS<br>Easy-to-make, beautiful timelines.",
          "text": "<p>TimelineJS is a populair tool from Knightlab. It has been used by more than 250,000 people to tell stories seen hundreds of millions of times, and is available in more than sixty languages. </p>"
        }
      }
      ......
    ]
}

    """
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": sysmsg},
            {"role": "user", "content": content},
        ]
    )
    return response.choices[0].message.content