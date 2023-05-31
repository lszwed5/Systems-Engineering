import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import neurokit2 as nk


duration = 100
sampling_rate = 1000
samples = duration * sampling_rate
interval = 5
offset = 0
offset_step = 0.1
fps = 1000
running = False


def move_left(event):
    global offset, running
    if not running:
        offset = offset - interval
        update(offset)
        plt.draw()


def move_right(event):
    global offset, running
    if not running:
        offset = offset + interval
        update(offset)
        plt.draw()


def reset(event):
    global offset
    offset = 0
    update(offset)
    plt.draw()


def stop(event):
    global running
    running = False
    animation.event_source.stop()


def resume(event):
    global running
    running = True
    animation.event_source.start()


def save(event):
    global running
    if not running:
        scroll_left_button.ax.set_visible(False)
        reset_button.ax.set_visible(False)
        resume_button.ax.set_visible(False)
        stop_button.ax.set_visible(False)
        save_button.ax.set_visible(False)
        scroll_right_button.ax.set_visible(False)

        plt.savefig('plot.png')

        scroll_left_button.ax.set_visible(True)
        reset_button.ax.set_visible(True)
        resume_button.ax.set_visible(True)
        stop_button.ax.set_visible(True)
        save_button.ax.set_visible(True)
        scroll_right_button.ax.set_visible(True)


def update(frame):
    global offset, x_data, y_data, running
    ax.clear()
    ax.set_xlim(offset, offset + interval)
    ax.set_ylim(np.min(y_data), np.max(y_data))
    line, = ax.plot(x_data, lw=2)
    line.set_data(x_data, y_data)
    ax.set_title(distance_text, loc="center")
    if running:
        offset += offset_step


y_data = nk.ecg_simulate(duration=duration, sampling_rate=sampling_rate,
                         method="simple")

fig, ax = plt.subplots()
x_data = np.linspace(0, duration, samples)
line, = ax.plot(x_data, lw=2)
ax.set_xlim(0, 5)
ax.set_ylim(np.min(y_data), np.max(y_data))

_, rpeaks = nk.ecg_peaks(y_data, sampling_rate=sampling_rate)
distances = np.diff(rpeaks['ECG_R_Peaks']) / 100

max_distance = np.max(distances) / 8
min_distance = np.min(distances) / 8
diff_distance = max_distance - min_distance

distance_text = f"Max distance: {max_distance:.3f}  Min distance: {min_distance:.3f}  Difference: {diff_distance:.3f} "


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
ax.set_title(distance_text, loc="center")
plt.show()
