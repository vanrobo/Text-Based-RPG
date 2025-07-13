### this is text-based-rpg interface 
import json
import time
import threading
import os
from dotenv import load_dotenv
import sys 

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
project_root_dir = os.path.dirname(current_dir)
generation_dir = os.path.join(project_root_dir, 'Generation')
sys.path.append(generation_dir)

import ai
import back_story
import world_gen 

load_dotenv()
variable_value = os.getenv("API_KEY")
if variable_value is None:
    print("API_KEY environment variable is not set.")
    print("You may get an API key from https://ai.google.dev/gemini-api/docs or https://aistudio.google.com/apikey and set it in the .env file.")
    api_key = input("Please enter your API key: ").strip()
    with open(".env", "w") as f:
        f.write(f"API_KEY={api_key}\n")
elif variable_value:
    print("key recognised\n\n")
    pass

#Loding player data
with open(r"Storage\settings.json") as data:
    settings = json.load(data)

with open (r"Storage\Saveslots\1\info.json") as slot:
    slot_1 = json.load(slot)

with open (r"Storage\Saveslots\2\info.json") as slot:
    slot_2 = json.load(slot)

with open (r"Storage\Saveslots\3\info.json") as slot:
    slot_3 = json.load(slot)

with open (r"Storage\Saveslots\4\info.json") as slot:
    slot_4 = json.load(slot)


    # print(slot_1, slot_2, slot_3, slot_4, config)

def animate(*text, delay=0.01,sep="", end="\n",between=None):

    combined_text = sep.join(map(str, text))

    if between is not None:
        for char in combined_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write(between) # put stsuff between characters, maybe like spaces.
            sys.stdout.flush()
            time.sleep(delay)
        print(end=end)
    else:
        for char in combined_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print(end=end)  # New line




def settingsa():

    text_to_speech = settings["text_to_speech"]
    font_size = settings["font_size"]
    font_family = settings["font_family"]
    font_colour = settings["font_colour"]

    while True:
        print(f"Which setting do you want to change: [enter a number] \
        \n\n\t(1) API_KEY \n\t(2) Text-To-Speech: {text_to_speech} \n\t(3) Font Size: {font_size} \n\t(4) Font Family: {font_family} \n\t(5) Font Colour: {font_colour} \n\t(6) Back \n\n")

        setting = input("You: ")

        if setting == "1":
            while True:
                api_key_new = input("Enter new api_key: \n\nYou: ")
                with open(".env", "w") as f:
                    f.write(f"API_KEY={api_key_new}\n")
                print("API_KEY updated")
                break
        
        elif setting == "2":
            while True:
                text_to_speech = input("Enable Text-To-Speech(Y/N): \n\nYou: ").lower().strip()

                if text_to_speech == "y" or text_to_speech == 'yes':
                    text_to_speech = True
                    print("Text-To-Speech Enabled")
                    break


                elif text_to_speech == 'n' or text_to_speech == "no":
                    text_to_speech = False
                    print("Text-To-Speech disabled")
                    break 

                else:
                    print("Please try again")

        elif setting == "3":
            font_size= int(input("Enter new font size: \n\nYou: "))
        

        elif setting == "4":
            font_family = input("Enter new font family: \n\nYou: ")
            

        elif setting == "5":
            font_colour = input("Enter new font colour: \n\nYou: ")

        
        elif setting == "6":
            print("Do you want to save your settings before leaving (Y/N)? \n")

            while True:

                setting_saving = input("You: ").strip().lower()

                if setting_saving == "yes" or setting_saving == 'y':
                    print("Saving settings..........")
                    settings["font_family"] = font_family
                    settings["font_size"] = font_size
                    settings["font_colour"] = font_colour
                    settings["text_to_speech"] = text_to_speech
                    print("Success")
                    return mainmenu()
                elif setting_saving == "no" or setting_saving == 'n':
                    print("Reverting settings.......")
                    return mainmenu()
                else:
                    print("Please try again")

        else:
            print("Please try again")



## if player decides to delete the saveslot
def deletion(saveslot_chosen):
        
        while True:
            print(f"Are you sure you want to delete \"{saveslot_chosen}\" (Y/N)\n\n")
            delete = input("You: ").lower().strip()

            if delete == "y" or delete == "yes":
                print("This action cannot be undone, do you still wish to continue (Y/N) \n\n")

                while True:
                    confirmation = input("You: ").lower().strip()

                    if confirmation == "y" or confirmation == "yes":
                        print("Deleting saveslot")
                        return
                    
                    elif confirmation == "n" or confirmation == "no":
                        print("Deletion Cancelled \nReturning to saveslot selection")
                        saveslot(slot_1["saveslot_name"],slot_2["saveslot_name"],slot_3["saveslot_name"],slot_4["saveslot_name"])

                        return
                    
                    else:
                        print("Please try again")
            

            elif delete == 'n' or delete == "no":
                print("Returning to saveslot selection")
                saveslot(slot_1["saveslot_name"],slot_2["saveslot_name"],slot_3["saveslot_name"],slot_4["saveslot_name"])

                return


            else:
                print("Please try again")


## Registiring player saveslot choice
def choose(saveslot_chosen):
    while saveslot_chosen["saveslot_created"] == True:
        choice = int(input("What do you want to do: \
                     \n\n\t(1) Continue\n\t(2) Edit\n\t(3) Delete\n\t(4) Back\n\nYou: "))
        
        if 0 < choice < 5:
            break

        else:
            print("Please try again")

    if choice == 1:
        print("When it all began.........")
        return
    
    elif choice == 2:
        print("What do you want to change:")
        return
    
    elif choice == 3:
        deletion(saveslot_chosen)
        return
    
    elif choice == 4:
        print("Returning to saveslot selection........")
        saveslot(slot_1,slot_2,slot_3,slot_4)
        return

    else:
        while True:
            continue_choice = input("Do you want to continue (Y/N): ").strip().lower()

            if continue_choice == "y" or continue_choice == "yes":
                name = input("Enter the name for your new saveslot: ")
                protag_name = input("Enter the name of your character: ")
                backstory_choice = input("Do you want to input a custom backstory (Optional) Y/N: ")
                backstory = input("Enter your custom backstory in short: ")
                break
            
            elif continue_choice == "n" or continue_choice == "no":
                print("Returning to saveslot selection........")
                saveslot(slot_1,slot_2,slot_3,slot_4)
                break

            else:
                print("Please try again")          
        return
        

def saveslot_description(sno):
    with open(f"Storage/Saveslots/{sno}/backstory.json") as slot:
        slot_info = json.load(slot)
        general_backstory = slot_info["about"]
        backstory = slot_info["backstory"]
        location = slot_info["location"]
        protagonist_name = slot_info["protagonist"]["name"]
        character_location = slot_info["protagonist"]["background"]
        protagonist_motivations = slot_info["protagonist"]["motivations"]
        unique_abilities = slot_info["protagonist"]["unique_abilities"]
        theme = slot_info["theme"]
        setting = slot_info["setting"]
        conflict = slot_info["conflict"]
        
        print('\n')
        animate("Press Enter to Continue...")
        input()
        animate("welcome to this world, ", end="\n")
        animate("soul",delay=0.5, between=" ")
        input()
        animate(protagonist_motivations, end="\n")
        input()
        time.sleep(0.5)
        animate( character_location, end="\n")
        input()
        time.sleep(0.5)
        animate(location, end="\n")
        input()
        time.sleep(0.5)
        animate("You have the following unique abilities: ", end="\n")
        print()
        for ability in unique_abilities:
            animate(f"\t- {ability}", end="\n")
        time.sleep(0.5)
        input()
        print()
        animate("Your backstory is as follows: ", end="\n")
        print()
        animate(general_backstory, end="\n")
        print()
        input()
        animate("And your detailed backstory is as follows: ", end="\n")
        print()
        animate(backstory, end="\n\n")
        input()
        time.sleep(2)
        animate("Basically, you see...")
        time.sleep(0.5)
        animate("Your world is basically: ", theme, end="\n")
        print()
        input()
        animate("The setting is: ", setting, end="\n")
        time.sleep(0.5)
        print()
        input()
        animate(conflict, end="\n")
        time.sleep(5)
        print()
        input()
        animate("Are you ready? ", end="\n")
        animate("You: ", delay=0.5, end="")
        input()
        print()
        animate("Let's begin your adventure!", end="\n")
        time.sleep(0.5)
        print("NOTE: THE GAMEPLAY HAS NOT YET BEEN IMPLEMENTED, SO THERE WILL BE AN ERROR IN 10 SECONDS")
        time.sleep(10)

    print(f'\n\n\t\t Slot {sno}: {slot_info["saveslot_name"]} \n\t\t Character: {slot_info["protagonist_name"]} \n\t\t Class: {slot_info["protagonist_class"]} \n\t\t Location: {slot_info["location"]} \n\t\t level: {slot_info["level"]} ')

def create_slot(sno=None):
    if sno is None:
        sno = input("Enter the saveslot number you want to create (1-4): ").strip()
        create_slot(sno)
    else:
        line = "-" * 50
        animate()
        animate("Greetings, Traveller", end="")
        animate("...", delay=0.5 )
        time.sleep(0.5)

        animate("Welcome to the world of Text-Based RPG")
        animate("You are about to create a brand new world")
        animate()
        animate("choose wisely...", delay=0.2,between=" ")
        animate()
        animate("This world will be your playground, your adventure, and your story")
        time.sleep(1)
        animate()
        animate("Input the name for your new saveslot: ")
        name = input("You: ").strip()
        animate()
        animate("Input the name of your character: ")
        protag_name = input("You: ").strip()
        animate()
        animate("Do you want to input a custom backstory (Optional) Y/N: ")
        backstory_choice = input("You: ").strip().lower()
        if backstory_choice == "y" or backstory_choice == "yes":
            print()
            animate("Enter your custom backstory in short: ")
            animate()
            
            backstory = input("You: ").strip()
            total_backstory = backstory + protag_name 
            back_story.generate_backstory(sno, total_backstory)
            animate("Backstory saved successfully!")
            world_gen.map_generation(sno)
            animate("World generated successfully!")

        else:
            print()
            back_story.generate_backstory(sno)
            animate("Random backstory generated successfully!")
            world_gen.map_generation(sno)
        animate("Saveslot created successfully!")
        saveslot_description(sno)

        
    


## Saveslot selection
def saveslot(Saveslot1,Saveslot2,Saveslot3,Saveslot4):
    while True: 
        if Saveslot1["saveslot_created"] == True:

            print(f' \n\n\t\t Slot 1: {Saveslot1["saveslot_name"]} \n\t\t Character: {Saveslot1["protagonist_name"]} \n\t\t Class: {Saveslot1["protagonist_class"]} \n\t\t Location: {Saveslot1["location"]} \n\t\t level: {Saveslot1["level"]} ')
        
        else:
            print("\n\n\t\t Slot 1: Create Slot")


        if Saveslot2["saveslot_created"] == True:

            print(f' \n\n\t\t Slot 2: {Saveslot2["saveslot_name"]} \n\t\t Character: {Saveslot2["protagonist_name"]} \n\t\t Class: {Saveslot2["protagonist_class"]} \n\t\t Location: {Saveslot2["location"]} \n\t\t level: {Saveslot2["level"]} ')
        
        else:
            print("\n\n\t\t Slot 2: Create Slot")      


        if Saveslot3["saveslot_created"] == True:

            print(f' \n\n\t\t Slot 3: {Saveslot3["saveslot_name"]} \n\t\t Character: {Saveslot3["protagonist_name"]} \n\t\t Class: {Saveslot3["protagonist_class"]} \n\t\t Location: {Saveslot3["location"]} \n\t\t level: {Saveslot3["level"]} ')
        
        else:
            print("\n\n\t\t Slot 3: Create Slot")
        

        if Saveslot4["saveslot_created"] == True:

            print(f'\n\n\t\t Slot 4: {Saveslot4["saveslot_name"]} \n\t\t Character: {Saveslot4["protagonist_name"]} \n\t\t Class: {Saveslot4["protagonist_class"]} \n\t\t Location: {Saveslot4["location"]} \n\t\t level: {Saveslot4["level"]} ')
        
        else:
            print("\n\n\t\t Slot 4: Create Slot")


        choice = input("\nTo choose a saveslot click a number 1-4 corresponding to your saveslot of choice.\nIf you wish to return press 5\nYou: ").strip().lower()

        if choice == "temp":
            saveslot_chosen = "temp"
            animate("Temporary saveslot created")
            sno="temp"
            create_slot(sno)
        elif int(choice) == 1:
            saveslot_chosen = Saveslot1
        elif int(choice) == 2:
            saveslot_chosen = Saveslot2
        elif int(choice) == 3:
            saveslot_chosen = Saveslot3
        elif int(choice) == 4:
            saveslot_chosen = Saveslot4        
        else:
            animate("Returning to main menu........")
            mainmenu()

    else:
        print("Please try again")
                 


## base interface person sees when they load into the game
def mainmenu():
 
    animate(r""" 
  _______        _      ____                     _   _____              
 |__   __|      | |    |  _ \                   | |  |  __ \             
    | | _____  _| |_   | |_) | __ _ ___  ___  __| |  | |__) | _ __   __ _ 
    | |/ _ \ \/ / __|  |  _ < / _` / __|/ _ \/ _` |  |  _  / | '_ \ / _` |
    | |  __/>  <| |_   | |_) | (_| \__ \  __/ (_| |  | | \ \ | |_) | (_| |
    |_|\___/_/\_\\__|  |____/ \__,_|___/\___|\__,_|  |_|  \_\| .__/ \__, |
                                                             | |     __/ |
                                                             |_|    |___/

""",delay=0.0001)
    animate("", "(1) Play", "(2) Settings", "(3) Credits", "(4) Exit", "Choose wisely...", sep = "\n\t", end = "\n\n\n")
   
    while True:
        mainOption = input("You: ").strip().lower()
    
        if mainOption == "1" or mainOption == "play" or mainOption == "p":
            saveslot(slot_1,slot_2,slot_3,slot_4)
            return            
            
        elif mainOption == "2" or mainOption == "setting" or mainOption == "settings" or mainOption == "s":
            settingsa()
            return

        elif mainOption == "3" or mainOption == "credit" or mainOption == "credits" or mainOption == "c":
            animate("Made by: Vanrobo and Valt20_20shu")
            mainmenu()

        elif mainOption == "4" or mainOption == "exit" or mainOption == "ex" or mainOption == "e":
            animate("Exiting the game...")
            sys.exit(0)
            
        else:
            animate("", "(1) Play", "(2) Settings", "(3) Credits", "(4) Exit", "Choose wisely...", sep = "\n\t", end = "\n\n\n")
        
    return


mainmenu()


