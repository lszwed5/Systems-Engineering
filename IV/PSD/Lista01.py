import neurokit2 as nk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


data = nk.data("bio_resting_5min_100hz")


ecg_signals, info = nk.ecg_process(data["ECG"], sampling_rate=100)

plt.rcParams["figure.figsize"] = (10, 5)
nk.ecg_plot(ecg_signals[:3000], sampling_rate=100)
fig = plt.gcf()
plt.tight_layout()
plt.show()


ecg = nk.data('ecg_1000hz.csv')
rpeaks, _ = nk.ecg_peaks(ecg, sampling_rate=1000)
ecg_rate = nk.ecg_rate(rpeaks, sampling_rate=1000, desired_length=len(ecg))

edr = nk.ecg_rsp(ecg_rate, sampling_rate=1000)
nk.signal_plot(edr)
fig1 = plt.gcf()
ax = plt.gca()
plt.title('EDR plot')
plt.subplots_adjust(left=0.15, bottom=0.3)


x_init = 10000
x_min = 10000
x_max = 50000

y_init = 4
y_min = 1
y_max = 10

x_slider_axe = plt.axes([0.15, 0.17, 0.7, 0.02])
y_slider_axe = plt.axes([0.15, 0.11, 0.7, 0.02])

x_slider = Slider(x_slider_axe, "x scale", x_min, x_max, valinit=x_init,
                  color="blue")
y_slider = Slider(y_slider_axe, "y scale", y_min, y_max, valinit=y_init,
                  color="blue")


def update(val):
    fig1.canvas.draw_idle()
    ax.set_ylim(-y_slider.val, y_slider.val)
    ax.set_xlim(0, x_slider.val)


x_slider.on_changed(update)
y_slider.on_changed(update)

plt.show()
