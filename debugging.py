import json


with open ("bigmap.json", "r") as big:
    world = json.load(big)


region = world["regions"]

for i in region:
    print("\n\n", i["name"], "\n\n")

    if i["type"] == "Continent":

        for j in i["nations"]:
            print("\n\t", j["name"], "\n")

            for k in j["cities"]:
                print("\t\t", k["name"])

    else:
        for j in i["locations"]:

            
            if j["type"] == "Water":
                print("\t Open Waters")

            else:
                print("\t", j["name"])
                for k in j["locations"]:
                    print("\t\t", k["name"])

