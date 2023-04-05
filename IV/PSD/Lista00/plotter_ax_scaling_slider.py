from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np


x_init = 1
x_min = 1
x_max = 10

y_init = 1
y_min = 1
y_max = 10


x = np.arange(-10, 10, 0.1)
f = 3 * np.cos(5 * np.cos(6 * np.pi * x) + 1 / 2 * np.sin(x))


fig, ax = plt.subplots()
plt.title('f(x) = 3 * cos(6 * pi * x) + 1/2 * sin(x)')
plt.subplots_adjust(left=0.15, bottom=0.3)
tot_plot, = plt.plot(x, f, 'b')
ax.set_ylim(-y_init, y_init)

x_slider_axe = plt.axes([0.15, 0.17, 0.7, 0.02])
y_slider_axe = plt.axes([0.15, 0.11, 0.7, 0.02])

x_slider = Slider(x_slider_axe, "x scale", x_min, x_max, valinit=x_init,
                  color="blue")
y_slider = Slider(y_slider_axe, "y scale", y_min, y_max, valinit=y_init,
                  color="blue")


def update(val):
    tot_plot.set_ydata(f)
    fig.canvas.draw_idle()
    ax.set_ylim(-y_slider.val, y_slider.val)
    ax.set_xlim(-x_slider.val, x_slider.val)


x_slider.on_changed(update)
y_slider.on_changed(update)
plt.show()
