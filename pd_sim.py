class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self, indice):
        print('indice',indice)
        if isinstance(indice,slice):
            print('slice',indice.start,indice.step,indice.stop)

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        titulo=titulo.strip()
        data[titulo]=[]
        titulos.append(titulo)
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem.strip())
    return DataFrame(data)

def loc (columna,fila=None): #Función para seleccionar por etiquetas (loc), identificar filas y columnas identificando si es un str, int, slice.
    dat=titulo
    fila=titulo

    
#prueba
d=read_csv('datos.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])
