from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are an AI assisstant who is expert human psychology. You understand the human nature and human brain. 

For the given input, analyse the question and break with the perspective of human psychology. 
Deeply analyse what the user want to ask, and aleast think 2-3 steps before giving an answer.

The steps are you get a user input, you analyse it, you try understand the psychology behind, you think, and then return an output with the explanation.

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always performs one step at a time and wait for the next input
3. Carfeully analyse the user query

Output Format:
{{step:"string",content:"string"}}

Example:
Input: How love is important for someone?
Output: {{step:"analyse", content:"Ok, you have asked a deep psychological question. Let me understand and think about it" }}
Output: {{step:"understand", content:"Understanding the psychology behind the question. What love is? How love actually happened? What happened when someone love someone else?"}}
Output: {{step:"think", content: "Thinking about the love based on human perpective and why it is important for someone"}}
Output: {{step:"result", content:"Love is crucial for human well-being. It forsters connection, reduce stress and improves mental and physical health. Ultimately love contributes to a richer and more fulfilling life."}}

"""

result = client.chat.completions.create(
    model="gemini-2.0-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system", "content":system_prompt},
        {"role":"user","content":"How love is important for someone?"},


        {"role":"assistant","content":json.dumps({"step": "analyse","content": "Okay, that's a really insightful question about the significance of love in a person's life. Let me break down the question to see what the user is trying to figure out."})},
        {"role":"assistant","content":json.dumps({"step": "understand", "content": "I need to consider love from different angles: What does love provide emotionally? How does it impact our sense of belonging and self-worth? Does its importance vary depending on personality or life stage?"})},
        {"role":"assistant","content":json.dumps({"step": "think", "content": "Okay, considering how fundamental love is to human psychology, it impacts our emotional, social, and even physical well-being. Let's structure an answer that reflects these different dimensions."})}
    ]
)

print(result.choices[0].message.content)

