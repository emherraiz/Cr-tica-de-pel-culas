class RepartoObservaciones:
    def __init__(self, df):
        self.df = df

    def cantidad_de_observaciones(self):
        return self.df['Cantidad'].sum()

    def media(self):
        temp = 0
        for i in range(len(self.df)):
            temp += self.df.iloc[i][0] * self.df.iloc[i][1]

        media = temp / cantidad_de_observaciones(self.df)

