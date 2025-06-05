### this is text-based-rpg interface 
import json
import time
import threading
import os
from dotenv import load_dotenv

load_dotenv()
variable_value = os.getenv("API_KEY")
if variable_value is None:
    print("API_KEY environment variable is not set.")
    api_key = input("Please enter your API key: ").strip()
    with open(".env", "w") as f:
        f.write(f"API_KEY={api_key}\n")
elif variable_value:
    print("key recognised\n\n")
    pass

#Loding player data
with open("data.json") as data:
    info = json.load(data)


    slot_1 = info["slot_1"]
    slot_2 = info["slot_2"]
    slot_3 = info["slot_3"]
    slot_4 = info["slot_4"]
    config = info["settings"]





def settings():

    text_speed = config["text_speed"]
    text_to_speech = config["text_to_speech"]
    font_size = config["font_size"]
    font_family = config["font_family"]
    font_colour = config["font_colour"]

    while True:
        print(f"Which setting do you want to change: [enter a number] \
        \n\n\t(1) Text Speed: {text_speed} \n\t(2) Text-To-Speech: {text_to_speech} \n\t(3) Font Size: {font_size} \n\t(4) Font Family {font_family} \n\t(5) Font Colour {font_colour} \n\t(6) Back \n\n")

        setting = input("You: ")

        if setting == "1":
            while True:
                text_speed = float(input("Enter new text speed: \n\nYou: "))

                if 0<text_speed<=1:
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
                    config["text_speed"] = text_speed
                    config["font_family"] = font_family
                    config["font_size"] = font_size
                    config["font_colour"] = font_colour
                    config["text_to_speech"] = text_to_speech

                    info["settings"] = config
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
                        saveslot(slot_1["Name"],slot_2["Name"],slot_3["Name"],slot_4["Name"])

                        return
                    
                    else:
                        print("Please try again")
            

            elif delete == 'n' or delete == "no":
                print("Returning to saveslot selection")
                saveslot(slot_1["Name"],slot_2["Name"],slot_3["Name"],slot_4["Name"])

                return


            else:
                print("Please try again")


## Registiring player saveslot choice
def choose(choice, saveslot_chosen):

    if choice == 1:
        print("When it all began.........")
        return
    
    elif choice == 2:
        print("What do you want to change:")
        return
    
    elif choice == 3:
        deletion(saveslot_chosen)
        return
    
    else:
        print("Returning to saveslot selection........")
        saveslot(slot_1["Name"],slot_2["Name"],slot_3["Name"],slot_4["Name"])
        return



## Saveslot selection
def saveslot(Saveslot1,Saveslot2,Saveslot3,Saveslot4):
    while True:
        choice = int(input(f"\nPlease select which saveslot that you want to choose: \
                       \n\n\t(1) {Saveslot1}\n\t(2) {Saveslot2}\n\t(3) {Saveslot3}\n\t(4) {Saveslot4}\n\nYou: "))
        
        if 0< choice < 5:
                                
            if choice == 1:
                saveslot_chosen = Saveslot1
            elif choice == 2:
                saveslot_chosen = Saveslot2
            elif choice == 3:
                saveslot_chosen = Saveslot3
            else:
                saveslot_chosen = Saveslot4

            while True:
                choice2 = int(input("What do you want to do: \
                             \n\n\t(1) Continue\n\t(2) Edit\n\t(3) Delete\n\t(4) Back\n\nYou: "))
                if 0 < choice2 < 5:

                    choose(choice2,saveslot_chosen)

                    return
                else:
                    print("Please try again")
        else:
            print("Please try again")
                 


## base interface person sees when they load into the game
def mainmenu():
 
    print(r""" 
  _______        _      ____                     _   _____              
 |__   __|      | |    |  _ \                   | |  |  __ \             
    | | _____  _| |_   | |_) | __ _ ___  ___  __| |  | |__) | _ __   __ _ 
    | |/ _ \ \/ / __|  |  _ < / _` / __|/ _ \/ _` |  |  _  / | '_ \ / _` |
    | |  __/>  <| |_   | |_) | (_| \__ \  __/ (_| |  | | \ \ | |_) | (_| |
    |_|\___/_/\_\\__|  |____/ \__,_|___/\___|\__,_|  |_|  \_\| .__/ \__, |
                                                             | |     __/ |
                                                             |_|    |___/

""")
    print("", "(1) Play", "(2) Settings", "(3) Credits", "(4) Exit", "Choose wisely...", sep = "\n\t", end = "\n\n\n")
   
    while True:
        mainOption = input("You: ").strip().lower()
    
        if mainOption == "1" or mainOption == "play" or mainOption == "p":
            saveslot(slot_1["Name"],slot_2["Name"],slot_3["Name"],slot_4["Name"])
            break
            
            
        elif mainOption == "2" or mainOption == "setting" or mainOption == "settings" or mainOption == "s":
            settings()
            break

        elif mainOption == "3" or mainOption == "credit" or mainOption == "credits" or mainOption == "c":
            print("Made by: Vanrobo and Valt20_20shu")
            break
            
        elif mainOption == "4" or mainOption == "exit" or mainOption == "ex" or mainOption == "e":
            print("Exiting the game...")
            break
        
        else:
            print("", "(1) Play", "(2) Settings", "(3) Credits", "(4) Exit", "Choose wisely...", sep = "\n\t", end = "\n\n\n")


mainmenu()


with open("data.json", "w") as data:
    json.dump(info, data, indent=4)

