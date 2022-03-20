import json


def save_json(obj, filename):
    j = json.dumps(obj)
    with open(filename, "w") as f:
        f.write(j)
