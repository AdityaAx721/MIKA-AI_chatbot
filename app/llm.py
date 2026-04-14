from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def get_response(messages):
    try:
        response = client.chat.completions.create(
            model="openchat/openchat-7b",
            messages=messages,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with primary model: {e}")
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=messages,
            max_tokens=200
        )
        return response.choices[0].message.content

    