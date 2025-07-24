# qjupyter/qdatasets.py

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_iris_binary():
    """
    Load a binary classification version of the Iris dataset (setosa vs versicolor).

    Returns:
        X_train, X_test, y_train, y_test (numpy arrays)
    """
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Use only setosa (0) and versicolor (1)
    mask = y < 2
    X = X[mask][:, :2]  # Use first 2 features for simplicity
    y = y[mask]

    X = StandardScaler().fit_transform(X)
    return train_test_split(X, y, test_size=0.2, random_state=42)


def load_xor():
    """
    Load a 2D XOR dataset.

    Returns:
        X_train, X_test, y_train, y_test (numpy arrays)
    """
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([0, 1, 1, 0])

    X = StandardScaler().fit_transform(X)
    return train_test_split(X, y, test_size=0.25, random_state=1)


def load_quantum_xor(encoded=True):
    """
    Load XOR dataset and optionally encode using angle features for QML.

    Args:
        encoded (bool): If True, return angle-encoded features (scaled to [0, pi])

    Returns:
        X_train, X_test, y_train, y_test (numpy arrays)
    """
    X_train, X_test, y_train, y_test = load_xor()

    if encoded:
        X_train = np.pi * X_train
        X_test = np.pi * X_test

    return X_train, X_test, y_train, y_test
