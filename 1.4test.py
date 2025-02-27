from zhipuai import ZhipuAI
client = ZhipuAI()  # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-zero-preview",  # 请填写您要调用的模型名称
    messages=[
        {"role": "system", "content": "不展示推理过程，直接输出结果"},
        {"role": "user", "content": "深圳是哪个省份的"}
    ],
    max_tokens=1200
)
print(response.choices[0].message.content)

print(response)