import json

with open ("data.json") as data: 
    info = json.load(data)
    skill = info["skill_level"]


print(skill)