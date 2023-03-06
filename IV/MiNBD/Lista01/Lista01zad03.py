from numpy.random import uniform, normal
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge


x_data = uniform(low=0.0, high=10, size=100)
y_func = normal(loc=0, scale=5, size=100)

dataset = np.array([[x, 20*x/3 + b + 10] for x, b in zip(x_data, y_func)]).T

plt.scatter(dataset[0], dataset[1])
plt.show()

# model chosen - linear function (y = ax + b)

X, Y = dataset

lin_reg = Ridge(alpha=0)
lin_reg_l2 = Ridge(alpha=100)
lin_reg.fit(X.reshape(-1, 1), Y)
lin_reg_l2.fit(X.reshape(-1, 1), Y)

X_dummy = np.linspace(start=X.min(), stop=X.max(), num=300).reshape(-1, 1)
Y_dummy_1 = lin_reg.predict(X_dummy)
Y_dummy_2 = lin_reg_l2.predict(X_dummy)
plt.scatter(X, Y)
plt.plot(X_dummy, Y_dummy_1, color='green', linewidth=3)
plt.plot(X_dummy, Y_dummy_2, color='red', linewidth=3)
plt.show()
