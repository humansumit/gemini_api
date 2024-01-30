import os
import PIL
import google.generativeai as genai
from dotenv import load_dotenv

# load all the environment variable from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

# QA on the picture
image = PIL.Image.open("1542272348-the-avengers.jpeg")
vision_model = genai.GenerativeModel("gemini-pro-vision")
response = vision_model.generate_content(["Explain the picture?", image])
print(response.text)


# Story generation from the image

vision_model = genai.GenerativeModel("gemini-pro-vision")
response = vision_model.generate_content(["Write a story from the picture", image])
print(response.text)


# assessing elements from the picture and creating new thing
image = PIL.Image.open("dsc03231.jpg")
vision_model = genai.GenerativeModel("gemini-pro-vision")
response = vision_model.generate_content(
    [
        "create dish from the ingredient present in the image, and mention its step by step preparation",
        image,
    ]
)
print(response.text)
