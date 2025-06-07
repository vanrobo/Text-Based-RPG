import os 
import time 
from dotenv import load_dotenv
import json
import prompts
import ai

with open(r"Storage\backstory.json") as backstory: 
    info = json.load(backstory)
    backstory = info["backstory"]
    protagonist = info["protagonist"]
    location = info["location"]

world_generation = "generate a world map" + "make sure to also add cities or villages" + prompts.world_gen + backstory + "\n\n" + protagonist["name"] + "\n\n" + location + "\n\n" + "Create a 10x10 map for this world with the theme of " + location + ".\n\n" + "**THIS IS A WORLD MAP, NOT A LOCAL VILLAGE MAP**"

print("Generating map...")

ai.generate(world_generation, r"Storage\map.json")