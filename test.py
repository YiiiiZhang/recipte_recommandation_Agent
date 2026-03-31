from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

resp = client.chat.completions.create(
    model="/path/to/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "user", "content": "Say hello in one short sentence."}
    ],
    temperature=0.2,
)

print(resp.choices[0].message.content)