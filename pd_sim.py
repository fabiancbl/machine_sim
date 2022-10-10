class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
    def __getitem__(self,i):
        print("Indice: ",i)
        if isinstance(i,slice):
            print("slice",i.start,i.stop,i.step)
    #Realizar lecturas según su posición
    def iloc(self,i):
        #if isinstance (i,slice):
         #   if isinstance (j,slice):
            
            
        if isinstance (i,int):
            titulos=self.data.keys()
            #for i in range(0,i):
             #print(self.data[i])
             #   a=d.data[i][0];

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline() #renglones
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo) #guarda titulos
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)

    
            
    
    
        
d=read_csv("datos.csv")    
#d=DataFrame([1,'a','b','c',8,9,10])
print(d.data)
d.iloc(5)





#                   A         B         C         D
##2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
#2013-01-02  1.212112 -0.173215  0.119209 -1.044236
#2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
#*2013-01-04  0.721555 -0.706771 -1.039575  0.271860
#2013-01-05 -0.424972  0.567020  0.276232 -1.087401
#2013-01-06 -0.673690  0.113648 -1.478427  0.524988
