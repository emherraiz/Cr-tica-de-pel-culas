from reparto_observaciones import RepartoObservaciones
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('criticas.csv')
    df = RepartoObservaciones(df)

    df.calcular_variables()
    media = df.gets('media')
    porcentaje, LI, LS = df.gets('rango', 1)
    print(f'Hay un {porcentaje} % de que nuestra puntuación se situe entre {LI} y {LS}')


