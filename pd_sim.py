import numpy as np

class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def T(self,d):
        # print("Hola Mundo"
        print(d.data)
        keys=dict.keys(d.data)
        

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo)
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)

# d1 = {
#   "Nombre": "Sara",
#   "Edad": 27,
#   "Documento": 1003882
# }

# df=pd.DataFrame()
# nombres = ['Juan', 'Laura', 'Pepe']
# edades = [42, 40, 37]
# df['Nombre'] = nombres
# df['Edad'] = edades
# print(df)

#prueba

d=read_csv('datos.csv')
d.T(d)