from reparto_observaciones import RepartoObservaciones
import pandas as pd
from math import sqrt, ceil

if __name__ == '__main__':
    df = pd.read_csv('criticas.csv')
    df = RepartoObservaciones(df)
    cantidad_de_observaciones()
