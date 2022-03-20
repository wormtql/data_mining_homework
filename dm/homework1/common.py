import csv
import json


class Item:
    def __init__(self, sharp, country, description, designation, points, price, province, region_1, region_2, taster_name):
        self.sharp = int(sharp)
        self.country = country if len(country) > 0 else None
        self.description = description if len(description) > 0 else None
        self.designation = designation if len(designation) > 0 else None
        self.points = float(points) if len(points) > 0 else None
        self.price = float(price) if len(price) > 0 else None
        self.province = province if len(province) > 0 else None
        self.region_1 = region_1 if len(region_1) > 0 else None
        self.region_2 = region_2 if len(region_2) > 0 else None
        self.taster_name = taster_name if len(taster_name) > 0 else None

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "id": self.sharp,
            "country": self.country,
            "description": self.description,
            "designation": self.designation,
            "points": self.points,
            "price": self.price,
            "province": self.province,
            "region_1": self.region_1,
            "region_2": self.region_2,
            "taster_name": self.taster_name
        }


def load_data_raw(limit=-1):
    results = []
    with open("data/archive/winemag-data-130k-v2.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if index == limit + 1:
                break

            sharp = row[0]
            country = row[1]
            description = row[2]
            designation = row[3]
            points = row[4]
            price = row[5]
            province = row[6]
            region_1 = row[7]
            region_2 = row[8]
            # print(type(region_2))
            taster_name = row[9]
            # print(sharp, country, description, designation, points, price, province, region_1, region_2, taster_name)

            item = Item(sharp, country, description, designation, points, price, province, region_1, region_2, taster_name)

            results.append(item.to_dict())
    return results


all_attributes = ["country", "description", "designation", "points", "price", "province", "region_1", "region_2", "taster_name"]

