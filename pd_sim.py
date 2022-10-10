

class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self,i):
        print ("indice",i) 
     
        
    def iloc(self,i):#Se debe crear la funcion iloc para el funcionamiento, de leer los datos segun su posicion 
        if isinstance (i,slice):
            if isinstance (j,slice):
           
        if isinstance (i,int):
            for i in range(0,i):
             print(self.data[i])
                a=d.data[i][0];

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
d=read_csv('datos.csv') #Se crearon los datos en formato csv para la lectura de los mismos
print(d.data)

titulos=d.keys()
valor=datos[titulos[0]]



