import json

with open (r"Storage\backstory.json") as backstory: 
    info = json.load(backstory)
    backstory = info["backstory"]

print(f"backstory:\n\n\t {backstory}") 