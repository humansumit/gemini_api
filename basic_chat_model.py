import os
from dotenv import load_dotenv
import google.generativeai as genai

# load all the environment variable from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


response = model.generate_content(
    "tell me newly discovered sub atomic particles, and its descriptions"
)

print(response.text)
