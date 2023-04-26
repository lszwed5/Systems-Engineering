from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animate(i):
    global x
    x += 0.01
    y = 3 * np.sin(2 * np.pi * x)
    data.append((x, y))
    ax.relim()
    ax.autoscale_view()
    line.set_data(*zip(*data))
    limes = list(zip(*data))
    plt.xlim(limes[0][-1] - 1, limes[0][-1])


fig, ax = plt.subplots()
x = 0
y = 3 * np.sin(2 * np.pi * x)
data = deque([(x, y)], maxlen=100)
line, = plt.plot(*zip(*data))
plt.ylim(-5, 5)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
