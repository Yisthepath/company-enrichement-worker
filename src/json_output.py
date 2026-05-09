import json


def output_json(file, object):
    with open(file, "w") as file:
        json.dump(object, file, indent="\t")
