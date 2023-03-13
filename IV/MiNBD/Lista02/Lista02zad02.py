import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import Interpolate


X_data = [0, 4/3, 8/3, 11/3]
Y_data = [-0.6, 0, 0.85, -1]

x = Interpolate.ask_for_input_to_interpolate(X_data)


interpolate = lagrange(X_data, Y_data)

X_dummy = np.linspace(0, 11/3, 100)
Y_dummy = interpolate(X_dummy)

y = interpolate(x)
print(f"The interpolated value for {x: 0.2f} is {y: 0.2f}")

plt.scatter(X_data, Y_data, color='tab:blue', label='samples')
plt.plot(X_dummy, Y_dummy, color="yellow", label='interpolation result')
plt.scatter(x, y, color='red')
plt.legend(shadow=True)
plt.show()
