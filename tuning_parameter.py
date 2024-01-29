import os
from dotenv import load_dotenv
import google.generativeai as genai

# load all the environment variable from .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

generation_config = genai.types.GenerationConfig(
    temperature=0,  # Consistent output in each iteration
    candidate_count=1,  # Number of generated responses to return
    stop_sequences=[
        "."
    ],  # The set of character sequences (up to 5) that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence. The stop sequence will not be included as part of the response.
    max_output_tokens=100,  # 	The maximum number of tokens to include in a candidate
    top_p=0.6,  # The maximum cumulative probability of tokens to consider when sampling
    top_k=10,  # The maximum number of tokens to consider when sampling
)

response = model.generate_content(
    "tell me newly discovered sub atomic particles, and its descriptions",
)

print(response.text)
