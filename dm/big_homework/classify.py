from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import chi2, SelectKBest, mutual_info_classif
from sklearn import tree
from .common import MyData


def get_precision(clf, data: MyData):
    predict = clf.predict(data.test_x)
    total = len(predict)
    correct = 0
    for index, value in enumerate(predict):
        truth = data.test_y[index] > 0.5
        pred = value > 0.5
        if pred == truth:
            correct += 1
    return correct / total


def feature_select(data: MyData):
    # fe = SelectKBest(mutual_info_classif, k=10)
    fe = SelectKBest(chi2, k=10)
    fe.fit(data.x, data.y)
    # x_new = fe.transform(data.x)

    sup = fe.get_support(True)
    # print(sup)
    names = []
    for index in sup:
        names.append(data.index2name[index])

    return names


def classify_svm(data: MyData, **kwargs):
    clf = svm.SVC(**kwargs)
    clf.fit(data.train_x, data.train_y)
    print("svm precision:", get_precision(clf, data))


def classify_random_forest(data: MyData):
    clf = RandomForestClassifier()
    clf.fit(data.train_x, data.train_y)
    print("random forest precision:", get_precision(clf, data))


def classify_decision_tree(data: MyData):
    clf = tree.DecisionTreeClassifier()
    clf.fit(data.train_x, data.train_y)
    print("decision tree precision:", get_precision(clf, data))
