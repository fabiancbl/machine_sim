class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
<<<<<<< HEAD
    def __getitem__(self, indice):
        print('indice',indice)
        if isinstance(indice,slice):
            print('slice',indice.start,indice.step,indice.stop)
=======
    def __getitem__(self,i):
        print ("Indice: ",i) 
>>>>>>> origin/JuanDavidR1028

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
<<<<<<< HEAD
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])
=======
#x=sum(map(len,d.data.values()))
#print(x)

for c in d.data.keys():
    print (d.data[c])
    
for t in d.data:
   print (t, ":", d.data[t])
   

  
print ("\n",funcion_tail("datos.csv",5))  
>>>>>>> origin/fabian048
