from numpy.random import uniform, normal
import matplotlib.pyplot as plt
import numpy as np
from PolynomialModel import PolynomialRegression


x_data = uniform(low=0.0, high=10, size=100)
y_func = normal(loc=0, scale=5, size=100)

dataset = np.array([[x, 20*x/3 + b + 10] for x, b in zip(x_data, y_func)]).T

plt.scatter(dataset[0], dataset[1])
plt.show()

# model chosen - linear function (y = ax + b)

X, Y = dataset


class LinearModel:
    """Class representing a linear data model."""

    def __init__(self):
        self.a = np.array([])

    @staticmethod
    def __add_constant__(matrix):
        """Add a column of ones to the right side of the matrix.

        This action enables model to learn a linear model with the b parameter.
        """
        return np.column_stack([matrix, np.ones((matrix.shape[0], 1))])

    def fit(self, X, Y):
        """Estimates linear parameters for the given dataset."""
        X, Y = np.array(X), np.array(Y)
        X_ext = self.__add_constant__(X)
        self.a = Y.T @ X_ext @ np.linalg.inv(X_ext.T @ X_ext)

    def show_params(self):
        """Print out model parameters."""
        print(f"a = {self.a[0]}")
        print(f"b = {self.a[1]}")

    def predict(self, X):
        """Returns the predictions for given X data."""
        X = np.array(X)
        X_ext = self.__add_constant__(X)
        return X_ext @ self.a.T

    def plot_regression(self, X, Y):
        """Plots the dataset along with the linear model."""
        X_dummy = np.linspace(start=X.min(), stop=X.max(), num=300)
        Y_dummy = self.predict(X_dummy)
        plt.scatter(X, Y)
        plt.plot(X_dummy, Y_dummy, color='red', linewidth=3)
        plt.show()


lin_mod = PolynomialRegression(1)
lin_mod.fit(X, Y)
lin_mod.show_params()
lin_mod.plot_regression(X, Y)
