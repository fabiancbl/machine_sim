class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
    def __getitem__(self,i):
        print("Indice: ",i)
        if isinstance(i,slice):
            print("slice",i.start,i.stop,i.step)
    #Realizar lecturas según su posición
    #def iloc(self,i,j):
     #   print("hola")
     
     
     
    def iloc(self,i,j):
        
        if isinstance(i,slice):
            if isinstance (j,slice):
                print("Indice: ",i)
                print("slice",i.start,i.stop,i.step)

        if isinstance (i,int):
            print("entero")
            titulos=self.data.keys()
            datos=self.data
            #a=datos(titulos[0])
            #print(a)
           # print(datos)
            #a=datos[0]
            #for j in range (len(titulos)):
             #   imprimir[j]=list(datos[1])
            #print(titulos)
           # print(a[0])
           # for j in range(len(titulos)):
                #print(titulos[j])
                #print(datos[i])
              
                 
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

    
            
    
    
datos="hola.csv"       
d=read_csv(datos)
#d=DataFrame([1,'a','b','c',8,9,10])
print(d.data)

d.iloc(5,0)





#                   A         B         C         D
##2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
#2013-01-02  1.212112 -0.173215  0.119209 -1.044236
#2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
#*2013-01-04  0.721555 -0.706771 -1.039575  0.271860
#2013-01-05 -0.424972  0.567020  0.276232 -1.087401
#2013-01-06 -0.673690  0.113648 -1.478427  0.524988
