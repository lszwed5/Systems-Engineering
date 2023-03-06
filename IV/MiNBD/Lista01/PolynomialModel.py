import numpy as np
import matplotlib.pyplot as plt


class PolynomialRegression:
    """Class representing a polynomial data model."""

    def __init__(self, degree):
        """Constructor.

        :param degree: The degree of the Polynominal Model to construct.
        :type degree: int
        """
        self.a = np.array([])
        self.degree = degree

    @staticmethod
    def __add_constant__(matrix):
        """Add a column of ones to the right side of the matrix.

        This action enables model to learn a linear model with the b parameter.
        After introducing the __extend_matrix__ method redundant, left for
        educational purposes.

        :param matrix: The X data matrix
        """
        return np.column_stack([matrix, np.ones((matrix.shape[0], 1))])

    @staticmethod
    def __extend_matrix__(matrix, degree):
        """Extends the given matrix to a correct number of dimensions.

        Given the degree of a polynomial model, transforms X data so that the
        model can compute a using the matrix implementation of the least
        squares method.

        :param matrix: The X data matrix
        :param degree: The degree of the Polynominal Model to construct.
        :type degree: int
        """
        degree += 1
        extended_matrix = []
        for i in range(matrix.shape[0]):
            for p in range(degree).__reversed__():
                extended_matrix.append(matrix[i]**p)
        return np.array(extended_matrix).reshape(matrix.shape[0], degree)

    def fit(self, X, Y):
        """Estimates polynomial parameters for the given dataset."""
        X, Y = np.array(X), np.array(Y)
        X_ext = self.__extend_matrix__(X, self.degree)
        self.a = Y.T @ X_ext @ np.linalg.inv(X_ext.T @ X_ext)

    def show_params(self):
        """Print out model parameters."""
        for i in range(self.a.shape[0]):
            print(f'a_{i} = {self.a[i]:0.4f}')

    def predict(self, X, degree):
        """Returns the predictions for given X data."""
        X = np.array(X)
        X_ext = self.__extend_matrix__(X, degree)
        return X_ext @ self.a.T

    def plot_regression(self, X, Y):
        """Plots the dataset along with the polynomial model."""
        X_dummy = np.linspace(start=X.min(), stop=X.max(), num=300)
        Y_dummy = self.predict(X_dummy, self.degree)
        plt.scatter(X, Y)
        plt.plot(X_dummy, Y_dummy, color='red', linewidth=3)
        plt.show()
