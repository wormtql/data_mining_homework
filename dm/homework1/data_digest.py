import matplotlib.pyplot as plt
import numpy as np

from .common import load_data_raw, all_attributes
from dm.common_utils import save_json


def freq(data, name):
    m = {}
    for item in data:
        value = item[name]
        if value is None:
            continue
        if value not in m:
            m[value] = 0
        m[value] += 1
    return m


def plot(f, title, filename, rotation=0):
    entries = []
    for label in f:
        entries.append((label, f[label]))

    labels = []
    values = []
    entries.sort(key=lambda x: x[0])
    for i in entries:
        labels.append(str(i[0]))
        values.append(i[1])

    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title(title)
    ax.bar(labels, values)
    ax.set_xticklabels(labels, rotation=rotation)
    fig.savefig(filename)
    # print(labels, values)
    # ax.bar(labels, values)
    # plt.plot(labels, values)


def get_none_count(data, name):
    count = 0
    for item in data:
        if item[name] is None:
            count += 1
    return count


def five_digest(data, name):
    arr = []
    for item in data:
        if item[name] is not None:
            arr.append(item[name])
    arr = np.array(arr)
    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "q1": np.quantile(arr, 0.25, interpolation="nearest"),
        "q3": np.quantile(arr, 0.75, interpolation="nearest"),
        "min": np.min(arr),
        "max": np.max(arr)
    }


def box_plot(data, name):
    arr = []
    for item in data:
        if item[name] is not None:
            arr.append(item[name])
    arr = np.array(arr)

    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title("box plot for " + name)
    ax.boxplot(arr)
    fig.savefig(f"output/homework1/box_plot_{name}.png")


def hist(data, name, bins=200):
    arr = []
    for item in data:
        if item[name] is not None:
            arr.append(item[name])
    arr = np.array(arr)

    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title("histogram for " + name)
    ax.hist(arr, bins=bins)
    fig.savefig(f"output/homework1/histogram_{name}.png")


def data_digest(data):
    output_dir = "output/homework1/"

    # 标称属性，给出每个可能取值的频数
    f1 = freq(data, "country")
    plot(f1, title="country distribution", filename="output/homework1/country_distrib_original.png", rotation=90)

    f2 = freq(data, "points")
    plot(f2, title="points distribution", filename="output/homework1/score_distrib_original.png")

    # 数值属性，给出5数概括及缺失值的个数
    none_count = []
    for name in all_attributes:
        none_count.append(get_none_count(data, name))
    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title("none count")
    ax.set_xticklabels(all_attributes, rotation=75)
    ax.bar(all_attributes, none_count)
    fig.savefig("output/homework1/none_count.png")

    # 5数概括
    five_points_points = five_digest(data, "points")
    save_json(five_points_points, output_dir + "5数概括_points.json")
    five_points_price = five_digest(data, "price")
    save_json(five_points_price, output_dir + "5数概括_price.json")

    # 盒图
    box_plot(data, "points")
    box_plot(data, "price")

    hist(data, "price")
