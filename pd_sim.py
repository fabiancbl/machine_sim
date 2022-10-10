class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data

def funcion_tail(arch, n,sep=';'):
	with open(arch) as f:
		lineas = [lineas.strip('\n') for lineas in f.readlines()]
	return lineas[-n:]
 
 
def read_csv(arch,sep=';'):
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
#prueba
d=read_csv('datos.csv')
#x=sum(map(len,d.data.values()))
#print(x)


for t in d.data:
   print (t, ":", d.data[t])
   

  
print ("\n",funcion_tail("datos.csv",5))  