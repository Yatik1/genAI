from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 

result = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role":"user","content":"Explain internet within 15 words"}
    ]
)

print(result.choices[0].message.content)