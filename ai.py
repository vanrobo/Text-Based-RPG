from google import genai
import os
from dotenv import load_dotenv
import prompts
import time # for note taking
# This file contains all the code for the AI 


load_dotenv()
api = os.getenv("API_KEY")

def clean(unfiltered_response): #remove ```json and ``` from the response
    if unfiltered_response.startswith("```json"):
        unfiltered_response = unfiltered_response.removeprefix("```json").strip()
    if unfiltered_response.endswith("```"):
        unfiltered_response = unfiltered_response.removesuffix("```").strip()
    return unfiltered_response

## gives storage and where to store the generated content
def generate(prompt,storage=None,*extra): # so 1st is the prompt fed in, the 2nd is the storage location, and the *extra is for any extra arguments that may be needed in the future.
    client = genai.Client(api_key=api)
    try:
        all_content = [prompt]
        if extra:
            all_content.extend(extra)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(all_content)
        )
        answer = clean(response.text) #removes ```json and ``` from the response
        if storage:
            with open(storage, "w") as file:
                file.write(answer) # writes the response to the file
        return answer
    except genai.errors.ClientError as e: # if no api key has an error
        print(f"Invalid argument: {e}\n")
        print("Please check your API key and ensure it is valid!\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def generateLite(prompt,storage=None,*extra): # same as above but for lite which has 30 rpm and 1500 req/day with lower latency
    client = genai.Client(api_key=api)
    try:
        all_content = [prompt]
        if extra:
            all_content.extend(extra)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=(all_content)
        )
        answer = clean(response.text) #removes ```json and ``` from the response
        if storage:
            with open(storage, "w") as file:
                file.write(answer) # writes the response to the file
        return answer
    except genai.errors.ClientError as e: # if no api key has an error
        print(f"Invalid argument: {e}\n")
        print("Please check your API key and ensure it is valid!\n")
    except Exception as e:
        print(f"An error occurred: {e}")

sno = 2

generate(prompts.main_story, rf"Saveslots\{sno}\backstory.json", "the protagonist is named shreyansh, who lives in delhi") # generates the backstory
