import json
import matplotlib.pyplot as plt
import pandas as pd


with open('weatherdata.json', 'r') as f:
    data = json.load(f)

weather = [[time, data] for time, data in
           zip(pd.to_datetime(data['hourly']['time']),
               (data['hourly']['temperature_2m']))]

font = {'size': 16}

plt.plot(pd.to_datetime(
    data['hourly']['time'], format='%Y-%m-%dT%H:%M'),
    data['hourly']['temperature_2m'],)

plt.title('Daily temperature in Wrocław for the January of 2023',
          fontdict=font, y=1.05)
plt.xlabel('Date', fontdict=font)
plt.ylabel('Temperature in C', fontdict=font)

plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.grid(which='major', alpha=0.5)

plt.show()
