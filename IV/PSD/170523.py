import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button


interval = 10
offset = 0
offset_step = 0.1
fps = 1000


def generate_x_y():
    x = np.linspace(-200, 1000, 12000)
    y = np.cos(x)
    return x, y


def move_left(event):
    global offset
    offset = offset - interval
    update(offset)
    plt.draw()


def move_right(event):
    global offset
    offset = offset + interval
    update(offset)
    plt.draw()


def reset(event):
    global offset
    offset = 0
    update(offset)
    plt.draw()


def stop(event):
    animation.event_source.stop()


def resume(event):
    animation.event_source.start()


def save(event):
    plt.savefig('plot.png')


def update(frame):
    global offset, x, y
    ax.clear()
    ax.set_xlim(offset, offset + 10)
    ax.set_ylim(-1.2, 1.2)
    line, = ax.plot([], [], lw=2)
    line.set_data(x, y)
    offset += offset_step


x, y = generate_x_y()

fig, ax = plt.subplots()
ax.set_xlim(0, 3 + 10)
line, = ax.plot([], [], lw=2)


scroll_left_button_ax = plt.axes([0.1, 0.06, 0.1, 0.05])
scroll_left_button = Button(scroll_left_button_ax, '<--')
scroll_left_button.on_clicked(move_left)

reset_button_ax = plt.axes([0.25, 0.06, 0.1, 0.05])
reset_button = Button(reset_button_ax, 'Reset')
reset_button.on_clicked(reset)

resume_button_ax = plt.axes([0.55, 0.06, 0.1, 0.05])
resume_button = Button(resume_button_ax, 'Resume')
resume_button.on_clicked(resume)

stop_button_ax = plt.axes([0.4, 0.06, 0.1, 0.05])
stop_button = Button(stop_button_ax, 'Stop')
stop_button.on_clicked(stop)

save_button_ax = plt.axes([0.7, 0.06, 0.1, 0.05])
save_button = Button(save_button_ax, 'Save')
save_button.on_clicked(save)

scroll_right_button_ax = plt.axes([0.85, 0.06, 0.1, 0.05])
scroll_right_button = Button(scroll_right_button_ax, '-->')
scroll_right_button.on_clicked(move_right)

plt.subplots_adjust(bottom=0.2)


animation = FuncAnimation(fig, update, frames=fps, interval=interval)
ax.set_title("Interactive cos(x) plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
