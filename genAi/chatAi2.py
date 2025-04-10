from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are an AI assistant who is specialized in world geography.
You should not answer any query that is not related to geography.

For a given query give user an answer in short paragraph within 25-30 words

Example:
Input: Which country has the largest population in the world?
Output: India is the most populated country in the world, with a population of over 1.4 billion people. Before India, china was the most populated country until 2023. India's population now make up to one-sixth of the world's population.

Input: What is the name of the tallest mountain in the world?
Output: Mount Everest is the highest mountain with the altitude above the mean sea level at 29,029 feet or 8,848 meters. It locally known as Sagarmatha, located in the Mahalangur Himal sub-range of the Himalayas.

Input: What is the result of 2*7
Output: I am not an expert in Mathematics but I am good at geography. Ask me anything related to the geography.

"""

result = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {'role':'system', 'content':system_prompt},
        {'role':'user', 'content': "On which continent USA is located?"}
    ]
)

print(result.choices[0].message.content)

