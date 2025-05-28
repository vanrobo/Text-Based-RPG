
def mainmenu ():
    print(" Welcome to Text-Based-RPG")
    print("", "(1) Play", "(2) Settings", "(3) Credits", sep = "\v\t", end = "\v\v\v")
    while True:
        choice = input("Enter input: ").lower().strip()
        if choice == "1" or choice == "play":
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
    print("Choose a saveslot: ")
    print(f"Saveslot 1: {saveslot1_name}, Saveslot 2: {saveslot2_name}")
    print('What do you want to do with the saveslot: ')
    print("Play, Exit or Delete")

mainmenu()