import os 
import time 
from dotenv import load_dotenv
import json
import prompts
import ai
import time




def map_generation():
    while True:
        try:
            sno = int(input("Enter a number from 1-4: "))
        
        except ValueError:
            print("Please try again")
            continue

        if sno < 1:
            print("Please try again")
            continue

        if sno > 4:
            print("Please try again")
            continue

        else:
            break

    with open(rf"Storage\Saveslots\{sno}\backstory.json") as backstory: 
        info = json.load(backstory)
        backstory = info["backstory"]
        protagonist_info = info["protagonist"]
        protagonist = protagonist_info["name"]+protagonist_info["background"]
        location = info["location"]
        theme_description = info["theme"]
        world_type = None
    world_generation = prompts.big_map + "\n\n" + prompts.specification_map_generation(world_type,backstory,location,protagonist,theme_description,"city")

    minworld_gen = prompts.big_map 

    generation = ai.generatelite(world_generation, rf"Storage\Saveslots\{sno}\map.json")
    for i in generation:
        print(i, end = '', flush=True)
        time.sleep(0.02)

    




map_generation()

