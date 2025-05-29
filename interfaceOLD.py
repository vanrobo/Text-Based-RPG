import time
import json

saveslot1_name = "Number 1"
saveslot2_name = "Number 2"

def mainmenu():
    print(" Welcome to Text-Based-RPG")
    print("", "(1) Play", "(2) Settings", "(3) Credits", sep = "\v\t", end = "\v\v\v")
    while True:
        choice = input("Choice: ").lower().strip()
        if choice == "1" or choice == "play":
            saveslot(saveslot1_name,saveslot2_name)
            print("Once upon a time")
            break
        elif choice == "2" or choice == "settings":
            print("Text Speed:")
            break 
        elif choice == "3" or choice == "credits":
            print("Vanbrobo and valtyshu")
            break
        
        else:
            print("please try again")
    


def quest(response,lore):
    print("Quest1:")
    print(f"Quest_Details: {response.text}")
    print("Lore")
    print(f"Lore: {lore.text}")

def saveslot(saveslot1_name, saveslot2_name):
    
    print(f"Saveslot 1: {saveslot1_name}, Saveslot 2: {saveslot2_name}")
    while True:
        choice = input("Choose a Saveslot: ")
        if choice == saveslot1_name or choice == saveslot2_name:
            while True: 
                choice2 = input('What do you want to do with the saveslot: \n Play, Exit or Delete: ' ).strip().lower()
                if choice2 == "play" or choice2 == "delete" or choice2 == "exit":
                    print(f"You chose to {choice2}")
                    return
                else:
                    print("Please try again")
            
        else:   
            print("Please try again")

mainmenu()


with open ("Text-Based-RPG\data.json", "r") as data:
    dice = json.load(data)
    slot_1 =  dice["slot_1"]
    print(slot_1["Name"])
