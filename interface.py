### this is text-based-rpg interface 
import json
import time


## base interface person sees when they load into the game

print()

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
            break
            
        elif mainOption == "2" or mainOption == "setting" or mainOption == "settings" or mainOption == "s":
            break

        elif mainOption == "3" or mainOption == "credit" or mainOption == "credits" or mainOption == "c":
            break

        else:
            print("", "(1) Play", "(2) Settings", "(3) Credits", "Choose wisely...", sep = "\n\t", end = "\n\n\n")


mainmenu()

