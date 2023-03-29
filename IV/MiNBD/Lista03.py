import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


"----------------------------------- Data -----------------------------------"

time_range = pd.date_range(start='2020-01-01', end='2020-12-31', freq='H')
y_data = np.round(np.cumsum(np.random.normal(0, 10, size=time_range.size),
                            axis=0), 2)
df = pd.DataFrame(y_data, index=time_range, columns=['x'])

df.plot()
plt.grid(which='major', alpha=0.5)
plt.show()

"---------------------------------- Zad 01 ----------------------------------"

x_norm = np.array(preprocessing.MinMaxScaler().fit_transform(
    y_data.reshape(-1, 1)))
df_norm = pd.DataFrame(x_norm, index=time_range, columns=['x'])

df_norm.plot()
plt.grid(which='major', alpha=0.5)
plt.show()

"---------------------------------- Zad 02 ----------------------------------"

x_stand = np.array(
    preprocessing.StandardScaler().fit_transform(y_data.reshape(-1, 1)))
df_stand = pd.DataFrame(x_stand, index=time_range, columns=['x'])

df_stand.plot()
plt.grid(which='major', alpha=0.5)
plt.show()

"---------------------------------- Zad 03 ----------------------------------"

x_scaled = np.array(preprocessing.MinMaxScaler((1, 10)).fit_transform(
    y_data.reshape(-1, 1)))
df_scaled = pd.DataFrame(x_scaled, index=time_range, columns=['x'])

df_scaled.plot()
plt.grid(which='major', alpha=0.5)
plt.show()

"-----------------------------------------------------------------------------"
