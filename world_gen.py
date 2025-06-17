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
        specifications = f"world_type: {world_type} backstory: {backstory}, location: {location}, protagonist: {protagonist}, theme_description: {theme_description}"
        Specifications3x3 = ai.generate(prompts.reasoning,r"Storage/temp.json", specifications)
        map = ai.generate(prompts.map3x3, rf"Storage\Saveslots\{sno}\world.json", Specifications3x3) # generates the world map
        
        generationcontinue = input("\nGenerate further:") # waits for the user to press enter before continuing

        if generationcontinue.lower() == "yes" or generationcontinue.lower() == "y":
            with open(rf"Storage/Saveslots/{sno}/world.json", "r") as data:
                map_data = json.load(data)
                map_tiles = []
                for tile in map_data['tiles']:
                    map_tiles += f"Tile ID: {tile['id']}, Category: {tile['category']}, Description: {tile['description']}\n)"
            
        
        else:
            return
#    thinking


#    world_generation = prompts.big_map + "\n\n" + prompts.specification_map_generation(world_type,backstory,location,protagonist,theme_description,"city")

#   minworld_gen = prompts.big_map 

    
#    for i in generation:
#       print(i, end = '', flush=True)
#       time.sleep(0.02)

    
map_generation()