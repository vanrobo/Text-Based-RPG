import google.generativeai as genai
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

if api:
    try:
        genai.configure(api_key=api)
        print("AI SDK Configured.")
    except Exception as e:
        print(f"Error configuring AI SDK: {e}. AI features may not work.")
        api = None # Disable AI if configuration fails
else:
    print("API_KEY not found in .env file. AI functionality will be disabled.")

def clean(unfiltered_response): #remove ```json and ``` from the response
    if unfiltered_response is None:
        return ""
    if unfiltered_response.startswith("```json"):
        unfiltered_response = unfiltered_response.removeprefix("```json").strip()
    if unfiltered_response.endswith("```"):
        unfiltered_response = unfiltered_response.removesuffix("```").strip()
    unfiltered_response = unfiltered_response.replace("\\n","")
    unfiltered_response = unfiltered_response.replace("\\","")
    return unfiltered_response

## gives storage and where to store the generated content
def generate(prompt,storage=None,*extra,loading=None): # so 1st is the prompt fed in, the 2nd is the storage location, and the *extra is for any extra arguments that may be needed in the future.
    if not api:
        print("AI is not configured due to missing API key or configuration error.")
        return "{ \"error\": \"AI not configured\" }" # Return a valid JSON string for error

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

        model_instance = genai.GenerativeModel(model_name="gemini-1.5-flash-latest") # Using a known common model
        # For "gemini-2.0-flash" - if this specific model name is needed and valid, it should be used.
        # model_instance = genai.GenerativeModel(model_name="gemini-2.0-flash")

        response = model_instance.generate_content(contents=all_content)
        answer = clean(response.text) #removes ```json and ``` from the response

        if storage:
            with open(storage, "w") as file:
                file.write(answer) # writes the response to the file
                
        return answer
    # except genai.errors.ClientError as e: # This specific error might change with new SDK versions
    #     print(f"AI Client Error: {e}\n")
    #     print("Please check your API key and ensure it is valid!\n")
    #     return "{ \"error\": \"AI Client Error\" }"
    except Exception as e:
        print(f"An error occurred during AI generation: {e}")
        return f"{{ \"error\": \"AI generation failed: {str(e).replace('\"','`')}\" }}"
    finally:
        if loader_thread and loader_thread.is_alive():
            generate_event.set()
            loader_thread.join(timeout=1)
            print("", end='\r')


def generatelite(prompt,storage=None,*extra,loading=None): # so 1st is the prompt fed in, the 2nd is the storage location, and the *extra is for any extra arguments that may be needed in the future.
    if not api:
        print("AI is not configured due to missing API key or configuration error.")
        return "{ \"error\": \"AI not configured\" }"

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

        # Assuming "gemini-2.0-flash-lite" should also use a common model or a validated specific one.
        # Using gemini-1.5-flash-latest as a placeholder.
        model_instance = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        # If "gemini-2.0-flash-lite" is a valid model name the user has access to:
        # model_instance = genai.GenerativeModel(model_name="gemini-2.0-flash-lite")

        response = model_instance.generate_content(contents=all_content)
        answer = clean(response.text) #removes ```json and ``` from the response
        if storage:
            with open(storage, "w") as file:
                file.write(answer) # writes the response to the file
        return answer
    # except genai.errors.ClientError as e: # This specific error might change
    #     print(f"AI Client Error: {e}\n")
    #     print("Please check your API key and ensure it is valid!\n")
    #     return "{ \"error\": \"AI Client Error\" }"
    except Exception as e:
        print(f"An error occurred during AI generation (generatelite): {e}")
        return f"{{ \"error\": \"AI generation failed (generatelite): {str(e).replace('\"','`')}\" }}"
    finally:
        if loader_thread and loader_thread.is_alive():
            generate_event.set()
            loader_thread.join(timeout=1)
            print("", end='')


def mapgen(prompt,*extra): #For Multilevel Map Gen
    if not api:
        print("AI is not configured due to missing API key or configuration error.")
        return "{ \"error\": \"AI not configured\" }"

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

        # Assuming "gemini-2.0-flash-lite" for mapgen as well.
        # Using gemini-1.5-flash-latest as a placeholder.
        model_instance = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        # If "gemini-2.0-flash-lite" is a valid model name the user has access to:
        # model_instance = genai.GenerativeModel(model_name="gemini-2.0-flash-lite")

        response = model_instance.generate_content(contents=all_content)
        answer = clean(response.text) #removes ```json and ``` from the response
        return answer
    
    # except genai.errors.ClientError as e: # This specific error might change
    #     print(f"AI Client Error: {e}\n")
    #     print("Please check your API key and ensure it is valid!\n")
    #     return "{ \"error\": \"AI Client Error\" }"
    except Exception as e:
        print(f"An error occurred during AI generation (mapgen): {e}")
        return f"{{ \"error\": \"AI generation failed (mapgen): {str(e).replace('\"','`')}\" }}"
    finally:
        if loader_thread and loader_thread.is_alive():
            generate_event.set()
            loader_thread.join(timeout=1)
            print("", end='')
