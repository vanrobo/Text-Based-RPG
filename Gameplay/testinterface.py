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

def animate(*text, delay=0.001,sep="", end="\n",between=None):

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


def input_animate(*text,delay=0.001,sep="", end="\n",between=None):

    combined_text = sep.join(map(str, text))

    if between is not None:
        for char in combined_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write(between) # put stsuff between characters, maybe like spaces.
            sys.stdout.flush()
            time.sleep(delay)
        print()
    else:
        for char in combined_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # New line
    
    val = input()

    return val




def settingsa():

    text_to_speech = settings["text_to_speech"]
    font_size = settings["font_size"]
    font_family = settings["font_family"]
    font_colour = settings["font_colour"]

    while True:
        animate(f"Which setting do you want to change: [enter a number] \
        \n\n\t(1) API_KEY \n\t(2) Text-To-Speech: {text_to_speech} \n\t(3) Font Size: {font_size} \n\t(4) Font Family: {font_family} \n\t(5) Font Colour: {font_colour} \n\t(6) Back \n\n")

        setting = input("You: ")

        if setting == "1":
            while True:
                api_key_new = input_animate("Enter new api_key: \n\nYou: ")
                with open(".env", "w") as f:
                    f.write(f"API_KEY={api_key_new}\n")
                animate("API_KEY updated")
                break
        
        elif setting == "2":
            while True:
                text_to_speech = input_animate("Enable Text-To-Speech(Y/N): \n\nYou: ").lower().strip()

                if text_to_speech == "y" or text_to_speech == 'yes':
                    text_to_speech = True
                    animate("Text-To-Speech Enabled")
                    break


                elif text_to_speech == 'n' or text_to_speech == "no":
                    text_to_speech = False
                    animate("Text-To-Speech Disabled")
                    break 

                else:
                    animate("Please try again")

        elif setting == "3":
            font_size= int(input_animate("Enter new font size: \n\nYou: "))
        

        elif setting == "4":
            font_family = input_animate("Enter new font family: \n\nYou: ")
            

        elif setting == "5":
            font_colour = input_animate("Enter new font colour: \n\nYou: ")

        
        elif setting == "6":
            animate("Do you want to save your settings before leaving (Y/N)? \n")

            while True:

                setting_saving = input("You: ").strip().lower()

                if setting_saving == "yes" or setting_saving == 'y':
                    animate("Saving settings..........")
                    settings["font_family"] = font_family
                    settings["font_size"] = font_size
                    settings["font_colour"] = font_colour
                    settings["text_to_speech"] = text_to_speech
                    with open (r"Storage\settings.json", "w") as set:
                        json.dump(settings, set, indent=4)
                    animate("Success")
                    return mainmenu()
                elif setting_saving == "no" or setting_saving == 'n':
                    animate("Reverting settings.......")
                    return mainmenu()
                else:
                    animate("Please try again")

        else:
            animate("Please try again")



## if player decides to delete the saveslot
def deletion(saveslot_chosen, sno):

    slotter_1 = slot_1
    slotter_2 = slot_2
    slotter_3 = slot_3
    slotter_4 = slot_4


    while True:
        animate(f"Are you sure you want to delete {saveslot_chosen["saveslot_name"]} (Y/N)\n\n")
        delete = input("You: ").lower().strip()

        if delete == "y" or delete == "yes":
            animate("This action cannot be undone, do you still wish to continue (Y/N) \n\n")

            while True:
                confirmation = input("You: ").lower().strip()

                if confirmation == "y" or confirmation == "yes":
                    animate("Deleting saveslot")
                    saveslot_chosen = {"saveslot_created": False, "saveslot_name": "", "date_of_creation": "", "protagonist_name": "","protagonist_class": "", "location": "", "level": ""}

                    if sno == 1:
                        slotter_1 = saveslot_chosen
                    elif sno == 2:
                        slotter_2 = saveslot_chosen
                    elif sno == 3:
                        slotter_3 = saveslot_chosen
                    elif sno == 4:
                        slotter_4 = saveslot_chosen
                    else:
                        pass
                    
                    with open (rf"Storage\Saveslots\{sno}\info.json", "w") as slot:
                        json.dump(saveslot_chosen, slot, indent=4)

                        
                    saveslot(slotter_1,slotter_2,slotter_3,slotter_4)

                    return
                
                elif confirmation == "n" or confirmation == "no":
                    animate("Deletion Cancelled \nReturning to saveslot selection")
                    saveslot(slotter_1,slotter_2,slotter_3,slotter_4)

                    return
                
                else:
                    animate("Please try again")
        

        elif delete == 'n' or delete == "no":
            animate("Returning to saveslot selection")
            saveslot(slot_1,slot_2,slot_3,slot_4)

            return


        else:
            animate("Please try again")


## Registiring player saveslot choice
def choose(saveslot_chosen, sno):
    choice = "pass"
    while saveslot_chosen["saveslot_created"] == True:
        choice = int(input_animate("What do you want to do: \
                     \n\n\t(1) Continue\n\t(2) Edit\n\t(3) Delete\n\t(4) Back\n\nYou: "))
        
        if 0 < choice < 5:
            break

        else:
            animate("Please try again")
    
    else:
        while True:
            continue_choice = input_animate("Do you want to continue (Y/N): ").strip().lower()

            if continue_choice == "y" or continue_choice == "yes":
                create_slot(saveslot_chosen,sno)
            elif continue_choice == "n" or continue_choice == "no":
                animate("Returning to saveslot selection........")
                saveslot(slot_1,slot_2,slot_3,slot_4)
                break

            else:
                animate("Please try again")          


    if choice == "pass":
        pass

    elif choice == 1:
        animate("When it all began.........")
        return
    
    elif choice == 2:
        animate("What do you want to change:")
        return
    
    elif choice == 3:
        deletion(saveslot_chosen, sno)
        return
    
    elif choice == 4:
        animate("Returning to saveslot selection........")
        saveslot(slot_1,slot_2,slot_3,slot_4)
        return

    
    else:
        animate("Please try again")
        
    return
        

def saveslot_description(sno):
    with open (f"Storage/Saveslots/{sno}/info.json") as slotting:
        slot_info = json.load(slotting)


    with open(f"Storage/Saveslots/{sno}/backstory.json") as slot:
        slot_backstory = json.load(slot)
        general_backstory = slot_backstory["about"]
        backstory = slot_backstory["backstory"]
        location = slot_backstory["location"]
        protagonist_name = slot_backstory["protagonist"]["name"]
        character_location = slot_backstory["protagonist"]["background"]
        protagonist_motivations = slot_backstory["protagonist"]["motivations"]
        unique_abilities = slot_backstory["protagonist"]["unique_abilities"]
        theme = slot_backstory["theme"]
        setting = slot_backstory["setting"]
        conflict = slot_backstory["conflict"]
        
        print('\n')
        animate("Press Enter to Continue...")
        input()
        animate("welcome to this world, ", end="\n")
        animate("soul",delay=0.05, between=" ")
        input_animate("Press Enter to continue... [you have to do this everytime]")
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
        animate("You: ", delay=0.05, end="")
        input()
        print()
        animate("Let's begin your adventure!", end="\n")
        time.sleep(0.5)
        animate("NOTE: THE GAMEPLAY HAS NOT YET BEEN IMPLEMENTED, SO THERE WILL BE AN ERROR IN 10 SECONDS")
        time.sleep(10)

    animate(f'\n\n\t\t Slot {sno}: {slot_info["saveslot_name"]} \n\t\t Character: {slot_info["protagonist_name"]} \n\t\t Class: {slot_info["protagonist_class"]} \n\t\t Location: {slot_info["location"]} \n\t\t level: {slot_info["level"]} ')

def create_slot(saveslot,sno=None):
    if sno is None:
        sno = input_animate("Enter the saveslot number you want to create (1-4): ").strip()
        create_slot(sno)
    else:
        line = "-" * 50
        print()
        animate("Greetings, Traveller", end="")
        animate("...", delay=0.05 )
        time.sleep(0.5)

        animate("Welcome to the world of Text-Based RPG")
        animate("You are about to create a brand new world")
        print()
        animate("choose wisely...", delay=0.02,between=" ")
        print()
        animate("This world will be your playground, your adventure, and your story")
        time.sleep(1)
        print()
        animate("Input the name for your new saveslot: ")
        while True:
            name = input("You: ").strip()
            if len(name) > 0:
                break
            else:
                print("Please enter saveslot name again")
        print()
        animate("Input the name of your character: ")
        while True:
                protag_name = input("You: ").strip()
                if len(protag_name) > 0:
                    break
                else:
                    print("Please enter your character's name again")
        print()
        animate("Do you want to input a custom backstory (Optional) Y/N: ")
        backstory_choice = input("You: ").strip().lower()
        if backstory_choice == "y" or backstory_choice == "yes":
            print()
            animate("Enter your custom backstory in short: ")
            print()
            
            backstory = input("You: ").strip()
            back_story.generate_backstory(sno,protag_name, backstory)
            animate("Backstory saved successfully!")
            world_gen.map_generation(sno)
            animate("World generated successfully!")

        else:
            print()
            back_story.generate_backstory_lite(sno,protag_name)
            animate("Random backstory generated successfully!")
            world_gen.map_generation(sno)
        animate("Saveslot created successfully!")
        saveslot["saveslot_created"] = True
        saveslot["saveslot_name"] = name
        saveslot["protagonist_name"] = protag_name
        with open (rf"Storage\Saveslots\{sno}\info.json", "w") as slot:
            json.dump(saveslot,slot, indent=4)


        saveslot_description(sno)

        
    


## Saveslot selection
def saveslot(Saveslot1,Saveslot2,Saveslot3,Saveslot4):
    while True: 
        if Saveslot1["saveslot_created"] == True:

            animate(f' \n\n\t\t Slot 1: {Saveslot1["saveslot_name"]} \n\t\t Character: {Saveslot1["protagonist_name"]} \n\t\t Class: {Saveslot1["protagonist_class"]} \n\t\t Location: {Saveslot1["location"]} \n\t\t level: {Saveslot1["level"]} ')
        
        else:
            animate("\n\n\t\t Slot 1: Create Slot")


        if Saveslot2["saveslot_created"] == True:

            animate(f' \n\n\t\t Slot 2: {Saveslot2["saveslot_name"]} \n\t\t Character: {Saveslot2["protagonist_name"]} \n\t\t Class: {Saveslot2["protagonist_class"]} \n\t\t Location: {Saveslot2["location"]} \n\t\t level: {Saveslot2["level"]} ')
        
        else:
            animate("\n\n\t\t Slot 2: Create Slot")      


        if Saveslot3["saveslot_created"] == True:

            animate(f' \n\n\t\t Slot 3: {Saveslot3["saveslot_name"]} \n\t\t Character: {Saveslot3["protagonist_name"]} \n\t\t Class: {Saveslot3["protagonist_class"]} \n\t\t Location: {Saveslot3["location"]} \n\t\t level: {Saveslot3["level"]} ')
        
        else:
            animate("\n\n\t\t Slot 3: Create Slot")
        

        if Saveslot4["saveslot_created"] == True:

            animate(f'\n\n\t\t Slot 4: {Saveslot4["saveslot_name"]} \n\t\t Character: {Saveslot4["protagonist_name"]} \n\t\t Class: {Saveslot4["protagonist_class"]} \n\t\t Location: {Saveslot4["location"]} \n\t\t level: {Saveslot4["level"]} ')
        
        else:
            animate("\n\n\t\t Slot 4: Create Slot")


        choice = input_animate("\nTo choose a saveslot click a number 1-4 corresponding to your saveslot of choice.\nIf you wish to return press 5\nYou: ").strip().lower()

        try:

            if choice == "temp":
                saveslot_chosen = "temp"
                animate("Temporary saveslot created")
                sno="temp"
                create_slot(sno)
            elif int(choice) == 1:
                saveslot_chosen = Saveslot1
                sno = 1
                
            elif int(choice) == 2:
                saveslot_chosen = Saveslot2
                sno = 2

                
            
            elif int(choice) == 3:
                saveslot_chosen = Saveslot3
                sno = 3
            
            elif int(choice) == 4:
                saveslot_chosen = Saveslot4
                sno = 4
                  
            
            elif int(choice) == 5:
                animate("Returning to main menu........")
                mainmenu()
                
            
            else:
                animate("Please try again")
        
        except Exception:
            animate("Please try again")
        
        choose(saveslot_chosen, sno)
        return


    else:
        animate("Please try again")
                 


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
            input_animate("Press Enter to return")
            mainmenu()

        elif mainOption == "4" or mainOption == "exit" or mainOption == "ex" or mainOption == "e":
            animate("Exiting the game...")
            sys.exit(0)
            
        else:
            animate("", "(1) Play", "(2) Settings", "(3) Credits", "(4) Exit", "Choose wisely...", sep = "\n\t", end = "\n\n\n")
        
    return


mainmenu()


