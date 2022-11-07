import json
import random
import argparse

class Generator:

    def __init__(self):
        pass

    def drawPracticeElement(self, jsonfile : str):
        """Draw a practice element randomly from a given 
        json file. The json file should assign weights indicating
        the probability associated with drawing each practice 
        element.

        :param jsonfile: Path to the json file w.r.t. the working dir.
        :type jsonfile: str

        Command-line usage:

        >>> python3 src/generator.py --json_file <json-file-path>

        For example:

        >>> python3 src/generator.py --json_file config/2022-W46.json


        """
        # open the json file
        f = open(jsonfile)
        data = json.load(f)
        keys = list(data.keys())


        # loop over keys and collect weights
        weights = []
        for key in keys:
            weights.append(data[key]['weight'])

        # draw an exercise
        exercise = random.choices(keys, weights)[0]
        print("Exercise:", exercise)

        # draw a practice element from the exercise's dict
        exercise_keys = data[exercise].keys()
        for key in exercise_keys:
            # skip if this key is the weight param
            if key == 'weight':
                continue
            
            # randomly select an element to add to output
            index = random.randrange(len(data[exercise][key]))
            print(key+":", str(data[exercise][key][index]))
            



if __name__ == "__main__":
    generator = Generator()
    # generator.generateScales("../config/scales.json")

    parser = argparse.ArgumentParser()
    parser.add_argument("--json_file")


    args = parser.parse_args()
    # print(args.json_file)
    generator.drawPracticeElement(args.json_file)