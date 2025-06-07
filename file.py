import json

with open (r"Storage\map.json") as backstory: 
    info = json.load(backstory)
    backstory = info["tiles"]

print(f"backstory:\n\n\t {backstory}") 

