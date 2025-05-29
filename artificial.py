from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("API_KEY")

client = genai.Client(api_key=api)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="generate a story for a soul in a corrupted world in india, a few lines only, but with a deep meaning"
)
print(response.text)
