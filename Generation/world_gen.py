import os
import time
from dotenv import load_dotenv
import json
import prompts
import ai
import time # time is imported twice, will remove one
# Assuming tile_type.py is in the parent directory or accessible via PYTHONPATH
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # Add parent dir to path
from tile_type import Tile, Forest, Mountain, City, Water # Import new tile classes




def multi_map_generation(): #multilevel generation
    while True:
        # while True: # Temporarily bypass input for testing
            # try:
                # sno = int(input("Enter a number from 1-4: "))
            #
            # except ValueError:
                # print("Please try again")
                # continue
            #
            # if sno < 1:
                # print("Please try again")
                # continue
            #
            # elif sno > 4:
                # print("Please try again")
                # continue
            #
            # else:
                # break
        sno = 1 # Hardcode for testing
        print(f"Using hardcoded save slot number: {sno}")

        i = 0 # Initialize i here to prevent UnboundLocalError in except block
        try:
            base_path = "Storage"
            save_slot_path = os.path.join(base_path, "Saveslots", str(sno))
            backstory_file_path = os.path.join(save_slot_path, "backstory.json")
            world_file_path = os.path.join(save_slot_path, "world.json")
            
            temp_storage_path = os.path.join(base_path, "Temp")
            temp_json_path = os.path.join(temp_storage_path, "temp.json")
            temp2_json_path = os.path.join(temp_storage_path, "temp2.json")

            # Ensure directories exist
            os.makedirs(save_slot_path, exist_ok=True)
            os.makedirs(temp_storage_path, exist_ok=True)

            with open(backstory_file_path, "r") as backstory_file:
                info = json.load(backstory_file)
                backstory = info["backstory"]
                protagonist_info = info["protagonist"]
                protagonist = protagonist_info["name"]+protagonist_info["background"]
                location = info["location"]
                theme_description = info["theme"]
                world_type = None
                specifications = f"world_type: {world_type} backstory: {backstory}, location: {location}, protagonist: {protagonist}, theme_description: {theme_description}"

            with open (world_file_path, "r") as world_file:
                world_info = json.load(world_file)
                world_tiles = world_info["tiles"]
                # i = 0 # Already initialized before try block
                Specifications3x3 = ai.generate(prompts.reasoning, temp_json_path, specifications)

                while i<9: # This loop assumes world_tiles has at least 9 elements.
                          # Add a check or ensure world.json is structured accordingly.
                    if i >= len(world_tiles):
                        print(f"Warning: world_tiles has only {len(world_tiles)} elements. Stopping at i={i}.")
                        break
                    world_places = world_tiles[i]
                    print("done till here x1")
                    ai_generated_map_str = ai.mapgen(prompts.map3x3, Specifications3x3)

                    with open (temp2_json_path, "w") as temp: # generates the world map
                        temp.write(ai_generated_map_str)

                    with open (temp2_json_path, "r") as temp:
                        # Assuming ai.mapgen returns a JSON string which is a list of tile-like dictionaries
                        ai_map_data_list = json.load(temp)

                    print("done till here x2")

                    processed_locations = []
                    if isinstance(ai_map_data_list, list): # Expecting a list of tile data from AI
                        for ai_tile_data in ai_map_data_list:
                            # This is a placeholder conversion.
                            # We need to know the actual structure of ai_tile_data
                            # and how it maps to our Tile objects.
                            tile_name = ai_tile_data.get("name", "Unknown Tile")
                            tile_description = ai_tile_data.get("description", "No description provided.")
                            tile_category = ai_tile_data.get("category", "Generic").lower() # e.g. "forest", "city"

                            tile_obj = None
                            if "forest" in tile_category:
                                tile_obj = Forest(name=tile_name, description=tile_description)
                            elif "mountain" in tile_category:
                                tile_obj = Mountain(name=tile_name, description=tile_description)
                            elif "city" in tile_category:
                                tile_obj = City(name=tile_name, description=tile_description)
                            elif "water" in tile_category or "lake" in tile_category or "ocean" in tile_category:
                                tile_obj = Water(name=tile_name, description=tile_description)
                            else:
                                # Default to a generic Tile if category is unknown
                                tile_obj = Tile(name=tile_name, description=tile_description)

                            processed_locations.append(tile_obj.to_dict())
                    else:
                        print(f"Warning: AI map data for world_place {i} is not a list as expected. Got: {type(ai_map_data_list)}")
                        # Fallback or error handling: store the raw data or an empty list
                        processed_locations = ai_map_data_list

                    world_places["locations"] = processed_locations
                    print("done till here x3")
                    world_tiles[i] = world_places
                    # print(world_places) # Becomes very verbose with full tile dicts
                    print(world_tiles)
                    i+=1
                
                world_info["tiles"] = world_tiles #Saves the generated information
         

            # Make sure world_file_path is defined before this point if this is where it's written
            with open(world_file_path, "w") as world_output_file:
                json.dump(world_info, world_output_file, indent=4)
                break # Exit the main while True loop after successful generation for one slot
                
        except FileNotFoundError as e:
            print(f"Error: A required file was not found: {e}")
            print(f"Attempted to access file for sno={sno} at path: {e.filename}")
            # Potentially create dummy files if they are missing and it's a first run scenario
            if not os.path.exists(backstory_file_path):
                print(f"Missing backstory file: {backstory_file_path}. Please create it.")
                # Example: Create a dummy backstory.json if it's critical for first run
                # with open(backstory_file_path, "w") as bf:
                #     json.dump({"backstory": "Default", "protagonist": {"name": "Player", "background": ""}, "location": "Start", "theme": "Default"}, bf)
                # print("Created a dummy backstory.json. Please customize and retry.")
            if not os.path.exists(world_file_path):
                 print(f"Missing world file: {world_file_path}. A new one will be created if generation completes.")
                 # Ensure world_info is initialized to prevent issues if we try to save a partial/empty one
                 world_info = {"tiles": [{"id": f"tile_{n}", "category": "empty", "description": "empty", "locations": []} for n in range(9)]}


        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__} - {e}")
            print(f"Current value of i: {i}") # i is now initialized
            # Consider whether to continue or break here. For testing, maybe break.
            break # Break on other exceptions too for now
            # continue # Original behavior was to continue, which might loop indefinitely on persistent errors

    # generationcontinue = input("Generate further:") # waits for the user to press enter before continuing
    generationcontinue = "no" # Hardcode for testing to prevent EOFError
    print(f"Skipping 'Generate further' prompt (hardcoded to '{generationcontinue}').")

    if generationcontinue.lower() == "yes" or generationcontinue.lower() == "y":
        # world_json_display_path = os.path.join("Storage", "Saveslots", str(sno), "world.json") # Original path construction
        world_json_display_path = world_file_path # Use the already defined path
        with open(world_json_display_path, "r") as data:
            map_data = json.load(data)
            map_tiles_display = "" # Renamed to avoid conflict with world_info["tiles"]
            for tile_info in map_data['tiles']: # Changed 'tile' to 'tile_info' for clarity
                # Ensure 'id', 'category', 'description' exist before trying to access them
                tile_id = tile_info.get('id', 'N/A')
                tile_category = tile_info.get('category', 'N/A')
                tile_desc = tile_info.get('description', 'N/A')
                map_tiles_display += f"Tile ID: {tile_id}, Category: {tile_category}, Description: {tile_desc}\n"
            print(map_tiles_display)
    else:
        return
    


#thinking

#    world_generation = prompts.big_map + "\n\n" + prompts.specification_map_generation(world_type,backstory,location,protagonist,theme_description,"city")

#   minworld_gen = prompts.big_map 

    
#    for i in generation:
#       print(i, end = '', flush=True)
#       time.sleep(0.02)

    



def map_generation():
    # while True: # Temporarily bypass input for testing
        # try:
            # sno = int(input("Enter a number from 1-4: "))
        #
        # except ValueError:
            # print("Please try again")
            # continue
        #
        # if sno < 1:
            # print("Please try again")
            # continue
        #
        # elif sno > 4:
            # print("Please try again")
            # continue
        #
        # else:
            # break
    sno = 1 # Hardcode for testing
    print(f"Using hardcoded save slot number in map_generation: {sno}")

    base_path = "Storage"
    save_slot_path = os.path.join(base_path, "Saveslots", str(sno))
    backstory_file_path = os.path.join(save_slot_path, "backstory.json")
    world_file_path = os.path.join(save_slot_path, "world.json") # For saving map output from ai.generate

    temp_storage_path = os.path.join(base_path, "Temp")
    temp_json_path = os.path.join(temp_storage_path, "temp.json") # For ai.generate reasoning output

    # Ensure directories exist
    os.makedirs(save_slot_path, exist_ok=True)
    os.makedirs(temp_storage_path, exist_ok=True)

    try:
        with open(backstory_file_path, "r") as backstory_file:
            info = json.load(backstory_file)
            backstory = info["backstory"]
            protagonist_info = info["protagonist"]
            protagonist = protagonist_info["name"]+protagonist_info["background"]
            location = info["location"]
            theme_description = info["theme"]
            world_type = None
            specifications = f"world_type: {world_type} backstory: {backstory}, location: {location}, protagonist: {protagonist}, theme_description: {theme_description}"

            Specifications3x3 = ai.generate(prompts.reasoning,temp_json_path, specifications)
            # The mapgen/ai.generate here saves its output to world_file_path
            generated_map_output = ai.generate(prompts.map3x3, world_file_path, Specifications3x3) # generates the world map

            # generationcontinue = input("Generate further:") # waits for the user to press enter before continuing
            generationcontinue = "no" # Hardcode for testing
            print(f"Skipping 'Generate further' prompt in map_generation (hardcoded to '{generationcontinue}').")

            if generationcontinue.lower() == "yes" or generationcontinue.lower() == "y":
                with open(world_file_path, "r") as data: # Read from the same file it just wrote to
                    map_data = json.load(data)
                    # This part assumes map_data is structured like world_info from multi_map_generation
                    # However, ai.generate directly writes the AI's response string.
                    # If map_data is just the AI string (potentially JSON), it won't have a 'tiles' key.
                    # This display logic might need adjustment based on what ai.generate actually saves.
                    if isinstance(map_data, dict) and 'tiles' in map_data:
                        map_tiles_display = ""
                        for tile_info in map_data['tiles']:
                            tile_id = tile_info.get('id', 'N/A')
                            tile_category = tile_info.get('category', 'N/A')
                            tile_desc = tile_info.get('description', 'N/A')
                            map_tiles_display += f"Tile ID: {tile_id}, Category: {tile_category}, Description: {tile_desc}\n"
                        print(map_tiles_display)
                    else:
                        print("Generated map data for display is not in the expected format (dict with 'tiles' key). Content:")
                        print(map_data)

            else:
                return
    except FileNotFoundError as e:
        print(f"Error in map_generation: A required file was not found: {e}")
        return
    except Exception as e:
        print(f"Error in map_generation: {type(e).__name__} - {e}")
        return

# Removed stray else: return block that was here, causing SyntaxError
        
multi_map_generation()