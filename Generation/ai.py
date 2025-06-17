from google import genai
import os
from dotenv import load_dotenv
import threading
import prompts
import time
import sys
# for note taking
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
def generate(prompt,storage=None,*extra,loading=None): # so 1st is the prompt fed in, the 2nd is the storage location, and the *extra is for any extra arguments that may be needed in the future.
    client = genai.Client(api_key=api)
    generate_event = threading.Event()

    def _internal_loader_animation():   
        animation_chars = ["Loading", "Loading.", "Loading..", "Loading..."]
        idx = 0
        sys.stdout.flush()

        while not generate_event.is_set():
            sys.stdout.write(f"\r{animation_chars[idx % len(animation_chars)]}   ")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.2)
        
        clear_line_animation = " " * 10  # Adjust number of spaces if your animation is longer
        sys.stdout.write(f"\r{clear_line_animation}\r") # Overwrite with spaces, then CR
        sys.stdout.flush()
        
    
    loader_thread = threading.Thread(target=_internal_loader_animation)
    loader_thread.daemon = True
    loader_thread.start()

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
    finally:
        if loader_thread and loader_thread.is_alive():
            generate_event.set()
            loader_thread.join(timeout=1)
            print("", end='\r')


def generatelite(prompt,storage=None,*extra,loading=None): # so 1st is the prompt fed in, the 2nd is the storage location, and the *extra is for any extra arguments that may be needed in the future.
    client = genai.Client(api_key=api)
    generate_event = threading.Event()

    def _internal_loader_animation():
        animation_chars = ["Loading", "Loading.", "Loading..", "Loading..."]
        idx = 0
        sys.stdout.flush()

        while not generate_event.is_set():
            sys.stdout.write(f"\r{animation_chars[idx % len(animation_chars)]}   ")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.2)
        
        clear_line_animation = " " * 10  # Adjust number of spaces if your animation is longer
        sys.stdout.write(f"\r{clear_line_animation}\r") # Overwrite with spaces, then CR
        sys.stdout.flush()
        
    
    loader_thread = threading.Thread(target=_internal_loader_animation)
    loader_thread.daemon = True
    loader_thread.start()

    try:
        all_content = [prompt]
        if extra:
            all_content.extend(extra)
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", contents=(all_content)
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
    finally:
        if loader_thread and loader_thread.is_alive():
            generate_event.set()
            loader_thread.join(timeout=1)
            print("", end='')

