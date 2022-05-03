from .common import *
from .visualize import *
from .classify import *


def big_homework():
    data = MyData()

    # plot_column(data, "ROA(A) before interest and % after tax", "ROA(C) before interest and depreciation before interest")
    # plot_column(data, "Operating Profit Growth Rate", "Total Asset Return Growth Rate Ratio")

    # pca_data = pca(data)
    # plot_pca(pca_data, data.y)

    # classify_svm(data, kernel="sigmoid")
    # classify_random_forest(data)
    # classify_decision_tree(data)
    # print(feature_select(data))

    plot_bar(data, "ROA(A) before interest and % after tax")
    plot_bar(data, "Debt ratio %")