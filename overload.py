import json

sno = int(input("Enter a number from 1-4: "))

with open(rf"Storage/Saveslots/{sno}/world.json", "r") as data:
    map_data = json.load(data)
    for tile in map_data['tiles']:
        print(f"Tile ID: {tile['id']}, Category: {tile['category']}, Description: {tile['description']})")
