class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self,i):
        print ("indice",i) 



def read_csv(filepath_or_buffer,sep=','):
    filepath_or_buffer = open(filepath_or_buffer)
    linea=filepath_or_buffer.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        titulo=titulo.strip()
        data[titulo]=[]
        titulos.append(titulo)
    for linea in filepath_or_buffer.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem.strip())
    return DataFrame(data)
            
        
#prueba
d=read_csv('datos.csv')
print(d.data)

