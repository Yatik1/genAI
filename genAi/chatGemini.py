from google import genai
from dotenv import load_dotenv
import os
# from google.genai import types    

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain internet within 15 words"
)

print(response.text)
