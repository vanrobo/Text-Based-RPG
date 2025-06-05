from google import genai
import os
from dotenv import load_dotenv
import prompts

load_dotenv()
api = os.getenv("API_KEY")

client = genai.Client(api_key=api)
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompts.main_story
    )
except exceptions as e:
    print(f"An error occurred: {e}")
    exit(1)
e


with open(r"Storage\backstory.json", "w") as file:
    file.write(prompts.clean(response.text))

with open(r"Storage\backstory.json", "r") as file:
    backstory = file.read()
    print(backstory)
