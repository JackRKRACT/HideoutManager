import json
from craft import craft
# Pass this class a JSON file containing Hideout craft information
# Generates craft array and Python JSON variable
class json_handler:

    craft_list = []

    # Pass exact directory to JSON file
    def __init__(self, json_file):
        print("Loading JSON")
        craft_file = open("crafts.json", "r")
        self.json_crafts = json.loads(craft_file.read())
        self.generateCrafts()

    # Updates local JSON file per initialization directory.
    def updateJSON(self):
            with open('crafts.json', 'w') as outfile:
                json.dump(self.json_crafts, outfile, indent=4)

    # Takes in loaded JSON and generates a list of crafts for each one within the file. 
    def generateCrafts(self):
        for key in self.json_crafts.keys():
            print("Called me")
            sub_dict = self.json_crafts.get(key)
            temp = craft(sub_dict, key)
            self.craft_list.append(temp)
