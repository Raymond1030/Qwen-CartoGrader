import os
import base64
import time

from openai import OpenAI


# 配置参数
FOLDER_PATH = "./MapFile"  # 图片文件夹路径
OUTPUT_FILE = "output.txt"   # 输出文件名
API_KEY = "your_api_key"  # API Key
ALLOWED_EXT = ['.jpg', '.jpeg', '.png']  # 支持的图片格式

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        base64image=base64.b64encode(image_file.read()).decode("utf-8")
    #关闭文件
    image_file.close()
    return base64image

def map_AI_Check(base64_image):
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    # 精简后的规则文本
    rule_text = """
    你是一个专业地图审查AI，请严格按以下规则检查地图问题，直接列出问题点，不需要解释原因或建议：

    **审查规则**
    1. 配色问题：饱和度过高/整体压抑
    2. 要素缺失：图框、比例尺、指北针等缺失
    3. 文字问题：压盖线要素/小数点超两位/缺少单位/中英混用
    4. 布局问题：主图不居中/大片空白/图例过大
    5. 其他问题：河流非蓝色/错别字/分层设色超过7级

    **输出要求**
    - 仅用中文列出存在的问题编号及问题解释（例："1.配色问题"）
    - 每个问题单独一行
    - 无问题时返回"审查通过"

    **错误类型编码**
    1-配色 2-要素 3-文字 4-布局 5-其他"
    """

    completion = client.chat.completions.create(
        model="qwen-vl-max-latest", #"qwen-omni-turbo",#qwen-vl-max-latest 
        messages=[
            {"role": "system", "content": [{"type": "text", "text": "你是一个专业的地图审查助手。"}]},
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url", 
                        "image_url":{"url":f"data:image/png;base64,{base64_image}"}
                    },
                    {
                        "type": "text",
                        "text": rule_text
                    },
                ],
            },
        ],
        modalities=["text"],  # 关闭音频输出减少负载
        stream=True,
        stream_options={"include_usage": True},
    )

    # # 处理响应流
    # with open("output.txt", "w", encoding="utf-8") as f:
    #     for chunk in completion:
    #         if chunk.choices and chunk.choices[0].delta.content:
    #             text = chunk.choices[0].delta.content
    #             print(text, end='', flush=True)
    #             f.write(text)
    # 获取响应
    result = ""
    for chunk in completion:
        if chunk.choices and chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content.strip()
    return result
    

if __name__ == "__main__":
     # 遍历文件夹
    for filename in os.listdir(FOLDER_PATH):
        # 提取学号和扩展名
        student_id, ext = os.path.splitext(filename)
        if ext.lower() not in ALLOWED_EXT:
            continue

        # 处理图片
        full_path = os.path.join(FOLDER_PATH, filename)
        print(f"正在处理学号 {student_id}...")
        print(full_path)
        
        base64_image = encode_image(full_path)
        print("图片编码完成")
        # 调用AI地图审查
        result = map_AI_Check(base64_image)
        
        # 写入结果
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{student_id}: {result}\n")
        
        # 避免频繁调用
        time.sleep(5)  # 根据API速率限制调整


