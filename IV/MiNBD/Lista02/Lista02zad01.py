import matplotlib.pyplot as plt
import Interpolate


X_data, Y_data = Interpolate.generate_data()

x = Interpolate.ask_for_input_to_interpolate(X_data)


x1, x2, y1, y2 = 0, 0, 0, 0
for i in range(len(X_data)):
    if X_data[i] <= x < X_data[i + 1]:
        x1 = X_data[i]
        y1 = Y_data[i]
        x2 = X_data[i + 1]
        y2 = Y_data[i + 1]
        break

y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
print(f"The interpolated value for {x: 0.2f} is {y: 0.2f}")

plt.plot(X_data, Y_data, color='yellow', label='interpolation result')
plt.scatter(X_data, Y_data, label='samples')
plt.scatter(x, y, color='red')
plt.show()
