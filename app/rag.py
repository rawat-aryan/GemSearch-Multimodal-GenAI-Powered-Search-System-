import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def handle_text_query(query):
    response = model.generate_content(query)
    return {"query": query, "response": response.text}
