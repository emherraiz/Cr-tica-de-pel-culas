from math import sqrt
class RepartoObservaciones:
    def __init__(self, df):
        self.df = df


    def cantidad_de_observaciones(self):
        self.cantidad = self.df['Cantidad'].sum()


    def calcular_media(self):
        temp = 0
        for i in range(len(self.df)):
            temp += self.df.iloc[i][0] * self.df.iloc[i][1]

        self.media = temp / self.cantidad


    def calcular_varianza_y_desviacion(self):
        temp = 0
        for i in range(len(self.df)):
            temp += self.df.iloc[i][1] *  pow((self.df.iloc[i][0] - self.media), 2)

        self.varianza = temp / self.cantidad
        self.desviacion = sqrt(self.varianza)


    def calcular_variables(self):
        self.cantidad_de_observaciones()
        self.calcular_media()
        self.calcular_varianza_y_desviacion()


    def entra_en_el_rango(self, LI, LS):
        temp = 0
        for i in range(len(self.df)):
            if self.df.iloc[i][0] >= LI and self.df.iloc[i][0] <= LS:
                temp += self.df.iloc[i][1]

        porcentaje = round(temp * 100 / self.cantidad)

        return porcentaje

    def rg(self, k):
        LI = round(self.media - k*self.desviacion, 2)
        LS = round(self.media + k*self.desviacion, 2)

        return self.entra_en_el_rango(LI, LS), LI, LS

    def gets(self, lo_que_se_quiere, k = 1):
        if lo_que_se_quiere.lower() == 'media':
            return self.media

        elif lo_que_se_quiere.lower() == 'varianza':
            return self.varianza

        elif lo_que_se_quiere.lower() == 'desviacion':
            return self.desviacion

        elif lo_que_se_quiere.lower() == 'rango':
            return self.rg(k)

