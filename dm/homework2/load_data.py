import json
from pathlib import Path

from dm.fp_tree.transaction import Transactions


def load_data():
    txt = Path("data/archive/winemag-data-130k-v2.json").read_text()
    raw = json.loads(txt)

    keys = ["points", "price", "region_1"]
    result = []
    for item in raw:
        valid = True
        new_item = {}
        for key in keys:
            if item[key] is None or item[key] == "":
                valid = False
                break
            else:
                new_item[key] = item[key]

        if valid:
            price = int(new_item["price"])
            if price < 100:
                new_item["price"] = "cheap"
            elif price < 1000:
                new_item["price"] = "expensive"
            else:
                new_item["price"] = "very expensive"
            result.append(new_item)

    return result


def load_fake_transaction():
    data = [
        "facdgimp",
        "abcflmo",
        "bfhjow",
        "bckspfam",
        "afcelpmn"
    ]

    result = Transactions()
    for t in data:
        result.add([c for c in t], 1)

    return result


def load_transaction():
    raw = load_data()

    result = Transactions()

    for item in raw:
        result.add([item["points"], item["price"], item["region_1"]], 1)

    # print(result.ts[0:10])
    return result
