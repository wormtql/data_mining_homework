import pandas as pd
import numpy as np
from sklearn.decomposition import KernelPCA
from sklearn.utils import shuffle


class MyData:
    def __init__(self):
        x, y = load_data()

        self.x = x
        self.normalized_x = normalize_x(x)
        self.y = y

        df = pd.read_csv("data/data.csv")
        index2name = {}
        name2index = {}
        for index, name in enumerate(df.columns):
            name = name.strip()
            index2name[index] = name
            name2index[name] = index

        self.index2name = index2name
        self.name2index = name2index

        length = len(x)
        print("length", length)
        train_length = int(0.7 * length)
        self.train_x = self.normalized_x[:train_length]
        self.train_y = self.y[:train_length]
        self.test_x = self.normalized_x[train_length:]
        self.test_y = self.y[train_length:]


def load_data():
    df = pd.read_csv("data/data.csv")
    df = shuffle(df)
    # for index, row in df.iterrows():
    #     print(len(row))
    #     print(row[1])
    #     break
    y = []
    x = []

    columns = df.shape[1]
    for index, row in df.iterrows():
        temp = []
        for i in range(columns):
            if i == 0:
                y.append(row[0])
            elif i != columns - 2:
                temp.append(row[i])
        x.append(temp)

    y = np.array(y)
    x = np.array(x)

    return x, y


def normalize_x(x):
    x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
    return x


def pca(data: MyData):
    pca = KernelPCA(n_components=2, kernel="poly")
    # pca = PCA(n_components=2)
    x = pca.fit_transform(data.x)
    return x
