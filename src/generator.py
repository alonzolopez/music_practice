import json
import random

class Generator:

    def __init__(self):
        pass

    def generateScales(self, scalesfile):
        # open the json file
        f = open(scalesfile)
        data = json.load(f)
        keys = data.keys()


        # loop over keys
        for key in keys:
            # randomly select an element to add to output
            index = random.randrange(len(data[key]))
            print(key+":", str(data[key][index]))
            



if __name__ == "__main__":
    generator = Generator()
    generator.generateScales("../config/scales.json")