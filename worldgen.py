import os 
import time 
from dotenv import load_dotenv
import json
import prompts
import ai

with open(r"Storage\backstory.json") as backstory: 
    info = json.load(backstory)
    backstory = info["backstory"]
    protagonist_info = info["protagonist"]
    protagonist = protagonist_info["name"]+protagonist_info["background"]
    location = info["location"]
    theme_description = info["theme"]


world_generation = prompts.world_gen + "\n\n" + prompts.specifications(backstory,location,protagonist,theme_description) 

print("Generating map...")

ai.generate(world_generation, r"Storage\map.json")