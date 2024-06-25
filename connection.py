import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
if 'GEMINI_API_KEY' not in os.environ:
    raise ValueError("Environment variable GEMINI_API_KEY is not set.")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

