import json


def save_json(obj, filename):
    j = json.dumps(obj, indent=4)
    with open(filename, "w") as f:
        f.write(j)
