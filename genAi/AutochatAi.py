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

messages = [
    {"role":"system","content":system_prompt}
]

query = input("> ")
messages.append({"role":"user","content":query})

while True:
    result = client.chat.completions.create(
        model="gemini-2.0-flash",
        response_format={"type":"json_object"},
        messages=messages
    )
 
    parsed_response = json.loads(result.choices[0].message.content)
    messages.append({"role":"assistant","content":json.dumps(parsed_response)})

    if parsed_response.get("step") != "result":
        print(f"🧠 : {parsed_response.get("content")}")
        continue
    
    print(f"🤖 : {parsed_response.get("content")}")
    break

