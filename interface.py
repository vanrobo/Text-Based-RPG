### this is text-based-rpg interface 
import json
import time


## base interface person sees when they load into the game

with open("Text-Based-RPG\data.json") as data:
    info = json.load(data)
    slot_1 = info["slot_1"]
    slot_2 = info["slot_2"]
    slot_3 = info["slot_3"]
    slot_4 = info["slot_4"]



print()



def saveslot(Saveslot1,Saveslot2,Saveslot3,Saveslot4):
    while True:
        choice = int(input(f"\nPlease select which saveslot that you want to choose: \
                       \n\n\t(1) {Saveslot1}\n\t(2) {Saveslot2}\n\t(3) {Saveslot3}\n\t(4) {Saveslot4}\n\nYou: "))
        if 0< choice < 5:
            print("Valid")
            break
        else:
            print("Please try again")
                 
    print(choice)

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
    print("", "(1) Play", "(2) Settings", "(3) Credits", "Choose wisely...", sep = "\n\t", end = "\n\n\n")
   
    while True:
        mainOption = input("You: ").strip().lower()
    
        if mainOption == "1" or mainOption == "play" or mainOption == "p":
            saveslot(slot_1["Name"],slot_2["Name"],slot_3["Name"],slot_4["Name"])
            break
            
        elif mainOption == "2" or mainOption == "setting" or mainOption == "settings" or mainOption == "s":
            break

        elif mainOption == "3" or mainOption == "credit" or mainOption == "credits" or mainOption == "c":
            break

        else:
            print("", "(1) Play", "(2) Settings", "(3) Credits", "Choose wisely...", sep = "\n\t", end = "\n\n\n")


mainmenu()

