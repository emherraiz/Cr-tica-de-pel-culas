import pandas as pd

df = pd.read_csv('criticas.csv', sep = ',' )
x = 0
for i in range(len(df)):
    x += df.iloc[i][0] * df.iloc[i][1]

media = x / sum(df.iloc[:][1])

print(media)
