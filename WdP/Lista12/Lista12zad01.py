import csv
from matplotlib import pyplot as plt

filename = r'C:\Users\lukas\OneDrive\Pulpit\Wszystko\Programy\INS\WdP\Lista12\ceny.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    woj, rice, roll, bread = [], [], [], []
    for row in reader:
        woj.append(str(row[0]))
        rice.append(float(row[1]))
        roll.append(float(row[2]))
        bread.append(float(row[3]))

alltogether = []
for i in range(len(rice)):
    alltogether.append(rice[i] + roll[i] + bread[i])

plt.style.use("seaborn")
fig, ax = plt.subplots(2, 2, figsize=(12, 7))
plt.rc("font", size=10)

ax[0][0].plot(woj[6:12], roll[6:12], c="r")
ax[0][0].plot(woj[6:12], rice[6:12], c="black")
ax[0][0].set_title("Porównanie cen")
ax[0][0].set_xlabel("Województwo")
ax[0][0].set_ylabel("Cena produktu [zł]")
ax[0][0].legend(labels=["Cena bułki", "Cena ryżu"], loc="upper right", fontsize=7)
plt.tick_params(axis='both', which='major', labelsize=8)
fig.autofmt_xdate()

ax[0][1].scatter(woj[10:18], roll[10:18])
ax[0][1].scatter(woj[10:18], bread[10:18])
ax[0][1].set_title("Ceny bułek i chleba")
ax[0][1].set_xlabel("Województwa")
ax[0][1].set_ylabel("Cena [zł]")
ax[0][1].legend(labels=["Cena chleba", "Cena bułki"], loc="upper right", fontsize=5)

ax[1][0].pie(roll[:6])
ax[1][0].set_title("Cena bułki w poszczególnych województwach")
ax[1][0].legend(labels=woj[:6], loc="upper right", fontsize=4)

ax[1][1].bar(woj[10:16], alltogether[10:16], color="purple")
ax[1][1].bar(woj[10:16], bread[10:16], color="yellow")
ax[1][1].set_xlabel("Województwo")
ax[1][1].set_ylabel("Cena [zł]")
ax[1][1].legend(labels=["Cena wszystkich towarów", "Cena samego chleba"], loc="upper right", fontsize=5)
ax[1][1].set_title("Cena wszystkich materiałów w poszczególnych województwach")

plt.tick_params(axis='both', which='major', labelsize=8)
plt.show()
