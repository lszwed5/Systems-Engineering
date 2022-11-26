import csv
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

filename = 'pojazdy.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    place, highs = [], []
    for row in reader:
        gmina = str(row[2])
        place.append(gmina)
        high = int(row[3])
        highs.append(high)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(place, highs, width=1, edgecolor="white", linewidth=0.7)

plt.title("Liczba pojazdów w poszczególnych gminach wojewódźtwa dolnośląskiego", fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Liczba Samochodów", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=6)

fig, ax = plt.subplots()
ax.plot(place, highs, linewidth=2.0)
plt.title("Liczba pojazdów w poszczególnych gminach wojewódźtwa dolnośląskiego", fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Liczba Samochodów", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=6)

fig, ax = plt.subplots()
ax.pie(highs , radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
plt.ylabel("Liczba Samochodów", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=6)

sizes = np.random.uniform(15, 80, len(highs))
colors = np.random.uniform(15, 80, len(highs))
fig, ax = plt.subplots()
ax.scatter(place, highs, s=sizes, c=colors, vmin=0, vmax=100)
plt.ylabel("Liczba Samochodów", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=3)
plt.show()
