import json
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
import numpy as np

with open('weatherdata.json', 'r') as f:
    data = json.load(f)

weather = [[time, data] for time, data in
           zip(pd.to_datetime(data['hourly']['time'], format='%Y-%m-%dT%H:%M'),
               (data['hourly']['temperature_2m']))]

font = {'size': 16}

"---------------------------------- Lab 01 ----------------------------------"

plt.plot(pd.to_datetime(
    data['hourly']['time'], format='%Y-%m-%dT%H:%M'),
    data['hourly']['temperature_2m'], )

plt.title('Daily temperature in Wrocław for the January of 2023',
          fontdict=font, y=1.05)
plt.xlabel('Date', fontdict=font)
plt.ylabel('Temperature in C', fontdict=font)

plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.grid(which='major', alpha=0.5)

plt.show()

"---------------------------------- Lab 02 ----------------------------------"

weather = [weather[i] for i in range(0, len(weather), 24)]
weather = np.array(weather[:-14]).T
plt.bar(weather[0], weather[1])
plt.plot(weather[0], weather[1], color='green')
plt.scatter(weather[0], weather[1], color='red')

plt.title('Daily temperature in Wrocław for the January of 2023',
          fontdict=font, y=1.05)
plt.xlabel('Date', fontdict=font)
plt.ylabel('Temperature in C', fontdict=font)

plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.25)

plt.show()

# 3 Plots of the same shape

fig, ax = plt.subplots(2, 2)
myFmt = DateFormatter("%d")
plt.title('Daily temperature in Wrocław for the January of 2023',
          fontdict=font, x=-0.12, y=2.3)

ax[0][1].plot(weather[0], weather[1], color='green')
ax[1][0].scatter(weather[0], weather[1], color='red')
ax[1][1].bar(weather[0], weather[1])

ax[0][0].set_axis_off()
ax[0][1].xaxis.set_major_formatter(myFmt)
ax[1][0].xaxis.set_major_formatter(myFmt)
ax[1][1].xaxis.set_major_formatter(myFmt)

plt.tick_params(axis='both', which='major', labelsize=8)
plt.show()

# 3 plots with different shapes

myFmt = DateFormatter("%d")
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=2)
ax2 = plt.subplot2grid((2, 2), (0, 1), colspan=1)
ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1)

ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
ax3.xaxis.set_major_formatter(myFmt)

ax1.plot(weather[0], weather[1], color='green')
ax2.scatter(weather[0], weather[1], color='red')
ax3.bar(weather[0], weather[1])

plt.tight_layout()

plt.show()
