import pandas as pd
from math import sqrt, ceil
import matplotlib.pyplot as plt

df = pd.read_csv('criticas.csv', sep = ',' )
temp = 0
for i in range(len(df)):
    temp += df.iloc[i][0] * df.iloc[i][1]

cantidad_de_observaciones = df['Cantidad'].sum()
media = temp / cantidad_de_observaciones

print(media)


temp = 0
for i in range(len(df)):
    temp += df.iloc[i][1] *  pow((df.iloc[i][0] - media), 2)

varianza = temp / cantidad_de_observaciones
desviacion = sqrt(varianza)

print(desviacion)

LI = ceil(media - desviacion)
LS = ceil(media + desviacion)
temp = 0
for i in range(len(df)):
    if df.iloc[i][0] >= LI and df.iloc[i][0] <= LS:
        temp += df.iloc[i][1]

print(f'El {round(temp * 100 / cantidad_de_observaciones)} % de las observaciones se encientran entre {LI} y {LS}')




fig, ax = plt.subplots()
ax.bar(df['Opinion'], df['Cantidad'])
ax.plot(media)
plt.show()



