from math import ceil, sqrt
class RepartoObservaciones:
    def __init__(self, df):
        self.df = df


    def cantidad_de_observaciones(self):
        self.cantidad = self.df['Cantidad'].sum()

    def media(self):
        temp = 0
        for i in range(len(self.df)):
            temp += self.df.iloc[i][0] * self.df.iloc[i][1]

        media = temp / self.cantidad
        self.media = media

    def get_media(self):
        return self.media

    def varianza_y_desviacion(self):
        temp = 0
        for i in range(len(self.df)):
            temp += self.df.iloc[i][1] *  pow((self.df.iloc[i][0] - self.media), 2)

        self.varianza = temp / self.cantidad
        self.desviacion = sqrt(self.varianza)

    def entra_en_el_rango(self, LI, LS):
        for i in range(len(self.df)):
            if self.df.iloc[i][0] >= LI and self.df.iloc[i][0] <= LS:
                temp += self.df.iloc[i][1]

        porcentaje = round(temp * 100 / self.cantidad)

        return porcentaje

    def rg(self, es_68_95_o_99 = 68):
        if int(es_68_95_o_99) == 68:
            k = 1
        elif int(es_68_95_o_99) == 95:
            k = 2
        else:
            k = 3



        LI = self.media - k*self.desviacion
        LS = self.media + k*self.desviacion
        return self.entra_en_el_rango(LI, LS), LI, LS

