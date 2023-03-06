from numpy.random import uniform, normal
import matplotlib.pyplot as plt
import numpy as np
from PolynomialModel import PolynomialRegression


x_data = uniform(low=-3, high=3, size=100)
y_func = normal(loc=0, scale=1, size=100)

dataset = np.array([[x, (3*x/4 + 1)**2 + b] for x, b in zip(x_data, y_func)]).T

plt.scatter(dataset[0], dataset[1])
plt.show()

# model chosen - square function (y = ax**2 + bx + c)

X, Y = dataset


sq_mod = PolynomialRegression(40)
sq_mod.fit(X, Y)
sq_mod.show_params()
sq_mod.plot_regression(X, Y)
