import numpy as np
import matplotlib.pyplot as plt
import copy


def hist(ax, data, name, title, bins=200):
    arr = []
    for item in data:
        if item[name] is not None:
            arr.append(item[name])
    arr = np.array(arr)

    ax.set_title(title)
    ax.hist(arr, bins=bins)


def gen_contrast_image(data, original_data, title, filename):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=[16, 9.6])
    hist(axes[0], data=original_data, name="price", title="original")
    hist(axes[1], data=data, name="price", title=title)
    fig.savefig(f"output/homework1/{filename}.png")


def data_remove_none(original_data, name):
    data = []
    for item in original_data:
        if item[name] is not None:
            data.append(item)
    return data


def data_highest_freq(original_data, name):
    arr = []
    for item in original_data:
        if item[name] is not None:
            arr.append(item[name])
    modal = np.argmax(np.bincount(arr))
    data = []
    for item in original_data:
        if item[name] is not None:
            data.append(item)
        else:
            temp = copy.deepcopy(item)
            temp[name] = modal
            data.append(temp)
    return data


def data_bayesian(original_data):
    m = {}
    for item in original_data:
        if item["points"] is not None and item["price"] is not None:
            score = item["points"]
            if score not in m:
                m[score] = []
            m[score].append(item["price"])

    modal = {}
    for score in m:
        modal[score] = np.argmax(np.bincount(m[score]))

    data = []
    for item in original_data:
        if item["price"] is not None:
            data.append(item)
        elif item["points"] is not None:
            temp = copy.deepcopy(item)
            temp["price"] = modal[item['points']]
            data.append(temp)
    return data


def run_contrast(original_data):
    data = data_remove_none(original_data, name="price")
    gen_contrast_image(data, original_data, title="remove none value", filename="contrast_remove_none")

    data = data_highest_freq(original_data, name="price")
    gen_contrast_image(data, original_data, title="use modal value", filename="contrast_use_modal")

    data = data_bayesian(original_data)
    gen_contrast_image(data, original_data, title="use bayesian", filename="contrast_bayesian")
