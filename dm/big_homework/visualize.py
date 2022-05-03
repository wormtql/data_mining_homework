import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .common import MyData


def plot_null(df: pd.DataFrame):
    columns = df.shape[1]

    null_count = []
    for i in range(columns):
        null_count.append(0)

    for index, row in df.iterrows():
        for i in range(columns):
            if pd.isna(row[i]) or pd.isnull(row[i]):
                null_count[i] += 1

    print(null_count)


def plot_column(data: MyData, name1: str, name2):
    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title(f"{name1}-{name2} Scatter")

    x = []
    y = []

    index1 = data.name2index[name1]
    index2 = data.name2index[name2]

    ax.scatter(data.x[:, index1], data.x[:, index2])
    fig.savefig(f"output/big_homework/scatter_{name1}_{name2}.png")


def plot_bar(data: MyData, name: str):
    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title(f"{name} Bar")

    index = data.name2index[name]
    d = data.x[:, index]
    ax.hist(d, bins=100)
    fig.savefig(f"output/big_homework/bar_{name}.png")


def plot_pca(pca_data, y):
    fig, ax = plt.subplots(figsize=[12.8, 9.6])
    ax.set_title("pca.png")

    pos = []
    neg = []
    for i in range(len(pca_data)):
        if y[i] > 0.5:
            pos.append(pca_data[i])
        else:
            neg.append(pca_data[i])
    pos = np.array(pos)
    neg = np.array(neg)

    ax.scatter(pos[:, 0], pos[:, 1], label="bankrupt")
    ax.scatter(neg[:, 0], neg[:, 1], label="otherwise")
    ax.legend()
    fig.savefig("output/big_homework/pca.png")
