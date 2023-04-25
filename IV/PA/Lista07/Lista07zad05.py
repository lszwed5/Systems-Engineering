from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft, fftfreq


A = [2]
a = [9*np.pi]
B = [6, 5]
b = [5*np.pi, 7*np.pi]


time = np.linspace(start=0, stop=10, num=2000)


def signal(t):
    return sum([A[i] * sin(a[i] * t) for i in range(len(A))]) + sum(
               [B[j] * cos(b[j] * t) for j in range(len(B))])


values = [signal(t) for t in time]
fourier_signal = rfft(values)

W = fftfreq(len(values), d=time[1] - time[0])

plt.figure()
plt.plot(time, values)
plt.show()

plt.figure()
plt.plot(W, fourier_signal)
left_lim, right_lim = -W.size, W.size
for i in range(len(fourier_signal)):
    if fourier_signal[i] > 100:
        left_lim = i
        break
for i in range(len(fourier_signal))[::-1]:
    if fourier_signal[i] > 100:
        right_lim = i
        break
plt.xlim(-fourier_signal[left_lim - 5], fourier_signal[right_lim + 5])
plt.show()


cut_f_signal = fourier_signal.copy()

to_filter = [[int(x) for x in range_.split("-")] for range_ in
             input("Enter the frequency ranges You would like to filter out\n "
                   "(Example: 4-8 7-9):\n").split(" ")]

for (start, stop) in to_filter:
    for i in range(len(cut_f_signal)):
        if start <= W[i] <= stop:
            cut_f_signal[i] = 0

cut_signal = irfft(cut_f_signal)


plt.figure()
plt.plot(time, cut_signal)
plt.show()

plt.figure()
plt.plot(W, cut_f_signal)
plt.xlim(-fourier_signal[left_lim - 5], fourier_signal[right_lim + 5])
plt.show()
