import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

x = np.arange(0.0, 1.0, 0.001)
y = 5 * np.cos(6 * np.pi * x)
l, = plt.plot(x, y)

ax.set_xlabel('X')
ax.set_ylabel('Y')

ax_freq = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_amplitude = plt.axes([0.25, 0.1, 0.65, 0.03])


freq = Slider(ax_freq, 'Frequency', 0.0, 20.0, 3)
amplitude = Slider(ax_amplitude, 'Amplitude', 0.0, 10.0, 5, valstep=1.0)


def update(val):
	f = freq.val
	a = amplitude.val
	l.set_ydata(a*np.sin(2*np.pi*f*x))


freq.on_changed(update)
amplitude.on_changed(update)

plt.show()
