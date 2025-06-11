import os 
import time 
from dotenv import load_dotenv
import json
import prompts
import ai
import time


sno= int(input("Enter a number from 1-4: "))

def map_generation(sno):
    with open(rf"Storage\Saveslots\{sno}\backstory.json") as backstory: 
        info = json.load(backstory)
        backstory = info["backstory"]
        protagonist_info = info["protagonist"]
        protagonist = protagonist_info["name"]+protagonist_info["background"]
        location = info["location"]
        theme_description = info["theme"]
        world_type = None
    world_generation = prompts.world_gen + "\n\n" + prompts.specification_worldgen(world_type,backstory,location,protagonist,theme_description) 
    generation = ai.generate(world_generation, rf"Storage\Saveslots\{sno}\map.json")
    for i in generation:
        print(i, end = '', flush=True)
        time.sleep(0.02)




map_generation(sno)

