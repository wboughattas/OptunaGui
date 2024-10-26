import pandas as pd
from sklearn import datasets


def load_iris_data():
    iris = datasets.load_iris()
    X, y = pd.DataFrame(iris.data, columns=iris.feature_names), pd.Series(iris.target)
    return X, y
