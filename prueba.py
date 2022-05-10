import pandas as pd
from math import sqrt

df = pd.read_csv('criticas.csv', sep = ',' )
x = 0
for i in range(len(df)):
    x += df.iloc[i][0] * df.iloc[i][1]

media = x / df['Cantidad'].sum()

print(media)
x = 0
for i in range(len(df)):
    x += df.iloc[i][1] *  pow((df.iloc[i][0] - media), 2)

varianza = x / df['Cantidad'].sum()
desviacion = sqrt(varianza)


print(varianza)
print(desviacion)



